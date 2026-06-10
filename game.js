/* Pixel's Code Quest — browser frontend.
 * Loads the same chapters.py / checks.py as the CLI version via Pyodide,
 * so the game logic stays in one place. */

const CAT_ART = {
  pixel:
`       /\\_/\\
      ( o.o )
       > ^ <
      /     \\
     ( PIXEL )
      \\_____/`,
  curious:
`       /\\_/\\
      ( o.o )
       > ? <`,
  happy:
`       /\\_/\\
      ( ^.^ )
       > w <    *purr*`,
  surprised:
`       /\\_/\\
      ( O_O )
       > ! <`,
  sleeping:
`       /\\_/\\
      ( -.- )
       > _ <    zzz...`,
  thinking:
`       /\\_/\\
      ( o.o )
       > . <    hmm`,
  sage:
`      /\\___/\\
     (  *.*  )
     (  =w=  )
      \\__v__/    "greetings, young one"`,
  victory:
`       /\\_/\\      ___
      ( ^.^ )    | * |
       > w <     |___|
      /     \\    trophy`,
};

const PROGRESS_KEY = 'pixel_quest_progress';

let pyodide = null;
let chapters = [];

const state = {
  chapterIdx: 0,
  challengeIdx: 0,
  hintsShown: 0,
  completedChapters: new Set(
    JSON.parse(localStorage.getItem(PROGRESS_KEY) || '[]')
  ),
};

const $ = (id) => document.getElementById(id);

async function init() {
  try {
    pyodide = await loadPyodide();
  } catch (e) {
    showFatal(`Couldn't load Pyodide: ${e.message}`);
    return;
  }

  $('loading-text').textContent = 'Fetching chapter scrolls...';

  const [checksSrc, chaptersSrc] = await Promise.all([
    fetch('pixel_quest/checks.py').then((r) => r.text()),
    fetch('pixel_quest/chapters.py').then((r) => r.text()),
  ]);

  pyodide.FS.writeFile('/checks.py', checksSrc);
  pyodide.FS.writeFile('/chapters.py', chaptersSrc);

  $('loading-text').textContent = 'Reading the chapters...';

  await pyodide.runPythonAsync(`
import sys, json, io, contextlib
sys.path.insert(0, '/')
import checks
import chapters as _chapters
CHAPTERS = _chapters.CHAPTERS

def get_metadata():
    out = []
    for ch in CHAPTERS:
        out.append({
            'id': ch['id'],
            'title': ch['title'],
            'cat_mood': ch.get('cat_mood', 'curious'),
            'story': ch['story'],
            'lesson': ch.get('lesson', ''),
            'example': ch.get('example', ''),
            'ending': ch.get('ending', ''),
            'challenges': [
                {
                    'title': c['title'],
                    'instructions': c['instructions'],
                    'starter': c.get('starter', ''),
                    'hints': c.get('hints', []),
                }
                for c in ch['challenges']
            ],
        })
    return json.dumps(out)

def run_code(ci, ji, code):
    c = CHAPTERS[ci]['challenges'][ji]
    namespace = dict(c.get('setup', {}))
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(code, '<your code>', 'exec'), namespace)
    except Exception as e:
        return json.dumps({
            'passed': False,
            'kind': 'error',
            'message': f"{type(e).__name__}: {e}",
            'stdout': buf.getvalue(),
        })
    stdout = buf.getvalue()
    for check in c['checks']:
        passed, msg = check(namespace)
        if not passed:
            return json.dumps({
                'passed': False,
                'kind': 'fail',
                'message': msg,
                'stdout': stdout,
            })
    return json.dumps({
        'passed': True,
        'kind': 'success',
        'message': c.get('success', 'Nice work!'),
        'stdout': stdout,
    })
`);

  const json = pyodide.runPython('get_metadata()');
  chapters = JSON.parse(json);

  // Resume at first unfinished chapter
  const firstIncomplete = chapters.findIndex(
    (ch) => !state.completedChapters.has(ch.id)
  );
  state.chapterIdx = firstIncomplete === -1 ? 0 : firstIncomplete;

  $('loading').hidden = true;
  $('game').hidden = false;
  showStory();
}

function showFatal(msg) {
  $('loading').innerHTML =
    `<p style="color:#a3284e">Pixel couldn't wake up.</p><pre>${msg}</pre>`;
}

function setCat(mood) {
  $('cat-art').textContent = CAT_ART[mood] || CAT_ART.curious;
}

function hideAllPanels() {
  [
    'story-panel',
    'lesson-panel',
    'challenge-panel',
    'ending-panel',
    'complete-panel',
    'menu-panel',
  ].forEach((id) => ($(id).hidden = true));
}

function showStory() {
  hideAllPanels();
  const ch = chapters[state.chapterIdx];
  setCat(ch.cat_mood);
  $('chapter-label').textContent = ch.title;
  $('story-text').textContent = ch.story;
  $('story-panel').hidden = false;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showLesson() {
  hideAllPanels();
  const ch = chapters[state.chapterIdx];
  setCat('sage');
  if (ch.lesson) {
    $('lesson-text').textContent = ch.lesson;
    $('lesson-example').textContent = ch.example || '';
    $('lesson-panel').hidden = false;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else {
    showChallenge();
  }
}

function showChallenge() {
  hideAllPanels();
  const ch = chapters[state.chapterIdx];
  const c = ch.challenges[state.challengeIdx];
  state.hintsShown = 0;
  setCat('thinking');
  $('challenge-title').textContent = `Challenge ${state.challengeIdx + 1}: ${c.title}`;
  $('challenge-instructions').textContent = c.instructions;
  $('code-input').value = c.starter || '';
  $('output').textContent = '';
  $('output').className = 'output';
  $('challenge-panel').hidden = false;
  $('code-input').focus();
}

function showEnding() {
  hideAllPanels();
  const ch = chapters[state.chapterIdx];
  setCat('happy');
  $('ending-text').textContent = ch.ending || '';
  $('ending-panel').hidden = false;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showComplete() {
  hideAllPanels();
  setCat('victory');
  $('chapter-label').textContent = 'You did it!';
  $('complete-panel').hidden = false;
}

function setOutput(text, kind) {
  const el = $('output');
  el.textContent = text;
  el.className = 'output ' + (kind || '');
}

function runCode() {
  const code = $('code-input').value;
  if (!code.trim()) {
    setOutput('No code yet. Write some Python and try again.', 'error');
    return;
  }
  pyodide.globals.set('_ci', state.chapterIdx);
  pyodide.globals.set('_ji', state.challengeIdx);
  pyodide.globals.set('_code', code);
  const result = JSON.parse(pyodide.runPython('run_code(_ci, _ji, _code)'));

  let display = result.message;
  if (result.stdout && result.stdout.trim()) {
    display = `print output:\n${result.stdout}\n${display}`;
  }

  if (result.passed) {
    setOutput(`*purr*  ${display}`, 'success');
    setCat('happy');
    setTimeout(advanceChallenge, 1400);
  } else if (result.kind === 'error') {
    setOutput(`*hiss*  ${display}`, 'error');
    setCat('surprised');
  } else {
    setOutput(`*tilt*  ${display}`, 'error');
    setCat('curious');
  }
}

function showHint() {
  const c = chapters[state.chapterIdx].challenges[state.challengeIdx];
  const hints = c.hints || [];
  if (state.hintsShown < hints.length) {
    setOutput(`*whisker twitch*  ${hints[state.hintsShown]}`, 'hint');
    state.hintsShown += 1;
  } else {
    setOutput("No more hints. Trust your whiskers!", 'hint');
  }
}

function skipChallenge() {
  setOutput('Pixel sighs and pads onward...', 'hint');
  setTimeout(advanceChallenge, 700);
}

function advanceChallenge() {
  const ch = chapters[state.chapterIdx];
  state.challengeIdx += 1;
  if (state.challengeIdx >= ch.challenges.length) {
    state.challengeIdx = 0;
    showEnding();
  } else {
    showChallenge();
  }
}

function nextChapter() {
  state.completedChapters.add(chapters[state.chapterIdx].id);
  saveProgress();
  state.chapterIdx += 1;
  state.challengeIdx = 0;
  if (state.chapterIdx >= chapters.length) {
    showComplete();
  } else {
    showStory();
  }
}

function saveProgress() {
  localStorage.setItem(
    PROGRESS_KEY,
    JSON.stringify(Array.from(state.completedChapters))
  );
}

function showMenu() {
  hideAllPanels();
  const list = $('chapter-list');
  list.innerHTML = '';
  chapters.forEach((ch, idx) => {
    const item = document.createElement('div');
    item.className = 'chapter-item';
    item.innerHTML =
      `<span>${ch.title}</span>` +
      (state.completedChapters.has(ch.id) ? '<span class="badge">done</span>' : '');
    item.onclick = () => {
      state.chapterIdx = idx;
      state.challengeIdx = 0;
      showStory();
    };
    list.appendChild(item);
  });
  $('menu-panel').hidden = false;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function resetProgress() {
  if (!confirm('Reset all progress? This clears completed chapters.')) return;
  state.completedChapters.clear();
  saveProgress();
  state.chapterIdx = 0;
  state.challengeIdx = 0;
  showStory();
}

function wireButtons() {
  $('story-continue').onclick = showLesson;
  $('lesson-continue').onclick = showChallenge;
  $('run-btn').onclick = runCode;
  $('hint-btn').onclick = showHint;
  $('skip-btn').onclick = skipChallenge;
  $('next-chapter').onclick = nextChapter;
  $('play-again').onclick = () => {
    state.chapterIdx = 0;
    state.challengeIdx = 0;
    showStory();
  };
  $('menu-btn').onclick = showMenu;
  $('close-menu').onclick = showStory;
  $('reset-progress').onclick = resetProgress;

  $('code-input').addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      runCode();
    }
    if (e.key === 'Tab') {
      e.preventDefault();
      const ta = e.target;
      const start = ta.selectionStart;
      const end = ta.selectionEnd;
      ta.value = ta.value.slice(0, start) + '    ' + ta.value.slice(end);
      ta.selectionStart = ta.selectionEnd = start + 4;
    }
  });
}

wireButtons();
init().catch((err) => {
  console.error(err);
  showFatal(err.message || String(err));
});
