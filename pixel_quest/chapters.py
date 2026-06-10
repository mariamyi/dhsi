"""Storyline chapters for Pixel's Code Quest.

Each chapter is a dict with:
  id, title, cat_mood, story, lesson, example, challenges, ending
Each challenge is a dict with:
  title, instructions, starter, hints, setup, checks, success
"""

from . import checks


CHAPTER_1 = {
    "id": "ch1_yarn",
    "title": "Chapter 1 — The Ball of Yarn",
    "cat_mood": "curious",
    "story": (
        "Pixel the cat was chasing a butterfly through a sunny meadow when "
        "the world suddenly went dark. The butterfly had fluttered into "
        "the Whisker Woods, a tangled forest where the trees whisper "
        "secrets in a language only cats and computers can understand.\n\n"
        "Lost and a little nervous, Pixel pads into a clearing. There, "
        "glowing softly, sits a ball of magical yarn. A voice rises "
        "from the yarn: 'Name me, little one, and I shall light your path.'"
    ),
    "lesson": (
        "In Python, you give names to things using VARIABLES. "
        "A variable is just a name that points at a value. "
        "You create one by writing the name, an equals sign, and the value."
    ),
    "example": (
        '# Give the name "pixel" to the value "cat"\n'
        'cat_name = "Pixel"\n'
        'age = 3\n'
        'is_hungry = True\n'
        '\n'
        '# You can use the variable later\n'
        'print(cat_name)   # prints: Pixel'
    ),
    "challenges": [
        {
            "title": "Name the yarn",
            "instructions": (
                "The yarn glows orange. Create a variable called "
                "'yarn_color' and set it to the string \"orange\"."
            ),
            "hints": [
                "Strings need quotes around them: \"orange\".",
                "It should look like: yarn_color = \"orange\"",
            ],
            "checks": [checks.has_var("yarn_color", "orange")],
            "success": "The yarn purrs and pulses with light. The path glows ahead!",
        },
        {
            "title": "Count your paws",
            "instructions": (
                "Pixel checks themselves over. Create a variable 'paws' "
                "equal to 4 (an integer, no quotes) and a variable "
                "'whiskers' equal to 12."
            ),
            "hints": [
                "Numbers don't need quotes: paws = 4",
                "Two separate lines: one for paws, one for whiskers.",
            ],
            "checks": [
                checks.has_var("paws", 4),
                checks.has_var("whiskers", 12),
                checks.var_type("paws", int),
            ],
            "success": "Everything in order. Pixel is whole and ready.",
        },
        {
            "title": "Pixel's profile",
            "instructions": (
                "Create three variables at once:\n"
                "  cat_name = \"Pixel\"\n"
                "  treats_eaten = 0\n"
                "  is_lost = True"
            ),
            "hints": [
                "True is a Python keyword, no quotes around it.",
                "Each variable on its own line.",
            ],
            "checks": [
                checks.has_var("cat_name", "Pixel"),
                checks.has_var("treats_eaten", 0),
                checks.has_var("is_lost", True),
            ],
            "success": "Pixel feels more like themselves now.",
        },
    ],
    "ending": (
        "The yarn unspools, drawing a glowing thread along the forest "
        "floor. Pixel follows it deeper into the woods."
    ),
}


CHAPTER_2 = {
    "id": "ch2_scrolls",
    "title": "Chapter 2 — The Whispering Scrolls",
    "cat_mood": "sage",
    "story": (
        "Following the yarn-thread, Pixel arrives at a tree hollow lined "
        "with paper scrolls. An old gray cat with silver whiskers looks "
        "up from the largest scroll.\n\n"
        "'I am Sage,' the old cat says. 'These scrolls hold the "
        "ancient cat-language of STRINGS. Master them, and you may "
        "speak with the forest itself.'"
    ),
    "lesson": (
        "Strings are pieces of text, wrapped in quotes. "
        "You can join them with +, repeat them with *, change them with "
        ".upper() and .lower(), and slot variables into them with f-strings."
    ),
    "example": (
        'greeting = "meow"\n'
        'loud = greeting.upper()         # "MEOW"\n'
        'twice = greeting + " " + greeting  # "meow meow"\n'
        '\n'
        'name = "Pixel"\n'
        'age = 3\n'
        'intro = f"I am {name}, age {age}"\n'
        '# intro is now: "I am Pixel, age 3"'
    ),
    "challenges": [
        {
            "title": "A loud purr",
            "instructions": (
                "Sage gives you the word \"purr\". Create a variable "
                "'greeting' set to \"purr\", then create 'loud_greeting' "
                "by calling .upper() on it. loud_greeting should be \"PURR\"."
            ),
            "hints": [
                "greeting = \"purr\"",
                "loud_greeting = greeting.upper()",
            ],
            "checks": [
                checks.has_var("greeting", "purr"),
                checks.has_var("loud_greeting", "PURR"),
            ],
            "success": "The scrolls rustle in approval.",
        },
        {
            "title": "Introduce yourself",
            "instructions": (
                "The variables 'name' and 'age' are already set for you "
                "(name = \"Pixel\", age = 3). Using an f-string, create a "
                "variable 'intro' that equals: I am Pixel, age 3"
            ),
            "setup": {"name": "Pixel", "age": 3},
            "hints": [
                "f-strings start with f: f\"...\"",
                "Put variables in curly braces: f\"I am {name}\"",
            ],
            "checks": [checks.has_var("intro", "I am Pixel, age 3")],
            "success": "Sage nods. 'You speak well, young one.'",
        },
        {
            "title": "Fix the typo",
            "instructions": (
                "A scroll says \"the dog purrs softly\" — clearly a "
                "mistake! The string 'scroll' is already set. Using "
                ".replace(), create a variable 'fixed' that replaces "
                "\"dog\" with \"cat\"."
            ),
            "setup": {"scroll": "the dog purrs softly"},
            "hints": [
                ".replace takes two arguments: the old word and the new one.",
                "fixed = scroll.replace(\"dog\", \"cat\")",
            ],
            "checks": [checks.has_var("fixed", "the cat purrs softly")],
            "success": "The forest sighs with relief. Order restored.",
        },
    ],
    "ending": (
        "Sage tucks the scrolls away. 'You have a quick tongue. The path "
        "ahead has more puzzles — choose wisely.'"
    ),
}


CHAPTER_3 = {
    "id": "ch3_treat",
    "title": "Chapter 3 — The Treat Decision",
    "cat_mood": "thinking",
    "story": (
        "The path forks at a stone bowl. The left fork smells of TUNA. "
        "The right fork smells of CHICKEN. A third path, barely visible, "
        "smells of NAP. Pixel must decide.\n\n"
        "A wooden sign reads: 'Only those who can decide may pass.'"
    ),
    "lesson": (
        "Python uses if / elif / else to make decisions. "
        "It runs the block under the first condition that is True."
    ),
    "example": (
        'weather = "sunny"\n'
        '\n'
        'if weather == "rainy":\n'
        '    plan = "stay inside"\n'
        'elif weather == "sunny":\n'
        '    plan = "nap in the sun"\n'
        'else:\n'
        '    plan = "look out the window"\n'
        '\n'
        '# plan is now "nap in the sun"'
    ),
    "challenges": [
        {
            "title": "Tuna or no?",
            "instructions": (
                "The variable 'treat' is set to \"tuna\". Write an if/else "
                "that sets a variable 'pixel_says' to \"yum\" when treat "
                "is \"tuna\", and \"no thanks\" otherwise."
            ),
            "setup": {"treat": "tuna"},
            "hints": [
                "Use == for comparison: if treat == \"tuna\":",
                "Don't forget the colon at the end of the if and else lines.",
                "Indent the body of the if/else with 4 spaces.",
            ],
            "checks": [checks.has_var("pixel_says", "yum")],
            "success": "Pixel licks their chops. Onward!",
        },
        {
            "title": "Reading the mood",
            "instructions": (
                "The variable 'hunger' is set (in this test, hunger = 4). "
                "Write if/elif/else code using 'hunger' to set 'action':\n"
                "  hunger >= 7  -> \"eat\"\n"
                "  hunger >= 3  -> \"play\"\n"
                "  else         -> \"nap\"\n"
                "Reference 'hunger' in your conditions (not a fixed number)."
            ),
            "setup": {"hunger": 4},
            "hints": [
                "Check >= 7 first, then >= 3, then else.",
                "if hunger >= 7:  /  elif hunger >= 3:  /  else:",
            ],
            "checks": [
                checks.has_var("action", "play"),
            ],
            "success": "The bowl glows. Pixel pounces playfully.",
        },
    ],
    "ending": (
        "Pixel pads down the tuna path, full belly leading the way."
    ),
}


CHAPTER_4 = {
    "id": "ch4_mice",
    "title": "Chapter 4 — The Great Mouse Hunt",
    "cat_mood": "surprised",
    "story": (
        "A meadow opens up, and Pixel's eyes go wide. MICE. Dozens of "
        "them, scampering across the grass.\n\n"
        "A whisper from the trees: 'Catch them all, in order, and the "
        "gate will open.'"
    ),
    "lesson": (
        "Loops let you repeat actions. The for loop walks through items "
        "(or numbers from range). The while loop keeps going as long as "
        "a condition is True."
    ),
    "example": (
        '# for loop with range\n'
        'total = 0\n'
        'for i in range(5):     # i = 0, 1, 2, 3, 4\n'
        '    total = total + i\n'
        '# total is now 10\n'
        '\n'
        '# while loop\n'
        'count = 3\n'
        'while count > 0:\n'
        '    count = count - 1\n'
        '# count is now 0'
    ),
    "challenges": [
        {
            "title": "Catch five mice",
            "instructions": (
                "Use a for loop with range to count to 5. Start with "
                "'caught = 0' and add 1 inside the loop, so by the end "
                "'caught' equals 5."
            ),
            "hints": [
                "Set caught = 0 before the loop.",
                "for i in range(5):  then  caught = caught + 1",
            ],
            "checks": [checks.has_var("caught", 5)],
            "success": "Five mice safely escorted to the mouse-village. Good cat.",
        },
        {
            "title": "Name the mice",
            "instructions": (
                "The list 'mice' is set for you. Use a for loop to count "
                "how many mice have names longer than 3 letters. Store "
                "the count in a variable called 'long_names'."
            ),
            "setup": {"mice": ["Ed", "Mo", "Lila", "Sam", "Tabitha", "Bo"]},
            "hints": [
                "len(name) gives the number of letters.",
                "Set long_names = 0, then loop over mice, adding 1 "
                "when len(name) > 3.",
            ],
            "checks": [checks.has_var("long_names", 2)],
            "success": "Lila and Tabitha tip their tiny hats.",
        },
        {
            "title": "Countdown to pounce",
            "instructions": (
                "Use a while loop. Start with 'pounce = 10'. Subtract 1 "
                "each loop until pounce reaches 0. (Don't go negative.)"
            ),
            "hints": [
                "while pounce > 0:",
                "Inside: pounce = pounce - 1",
            ],
            "checks": [checks.has_var("pounce", 0)],
            "success": "POUNCE! Direct hit. The gate creaks open.",
        },
    ],
    "ending": (
        "The meadow gate swings wide. Pixel slips through, fur ruffled "
        "and proud."
    ),
}


CHAPTER_5 = {
    "id": "ch5_council",
    "title": "Chapter 5 — The Cat Council",
    "cat_mood": "sage",
    "story": (
        "Beyond the gate, Pixel finds a circle of cats sitting around an "
        "ancient stone. The eldest cat speaks: 'Every cat in our "
        "council is kept in a list. To join us, you must learn the way "
        "of lists.'"
    ),
    "lesson": (
        "Lists hold multiple items in order. You can grab items by "
        "position (starting at 0), add items with append, count them "
        "with len, and slice out a range."
    ),
    "example": (
        'cats = ["Mittens", "Whiskers", "Boots"]\n'
        '\n'
        'first = cats[0]        # "Mittens"\n'
        'last = cats[-1]        # "Boots"\n'
        'cats.append("Pixel")   # cats now has 4 items\n'
        'count = len(cats)      # 4\n'
        'two = cats[0:2]        # ["Mittens", "Whiskers"]'
    ),
    "challenges": [
        {
            "title": "Join the council",
            "instructions": (
                "The list 'council' is set with three cat names. Append "
                "\"Pixel\" to the end, then store the new length in a "
                "variable called 'size'."
            ),
            "setup": {"council": ["Mittens", "Whiskers", "Boots"]},
            "hints": [
                "council.append(\"Pixel\")",
                "size = len(council)",
            ],
            "checks": [
                checks.custom(
                    lambda ns: ns.get("council") == ["Mittens", "Whiskers", "Boots", "Pixel"],
                    "council should end with Pixel appended.",
                ),
                checks.has_var("size", 4),
            ],
            "success": "The council nods. You are one of them now.",
        },
        {
            "title": "Eldest and youngest",
            "instructions": (
                "The list 'elders' is sorted oldest first. Set 'eldest' "
                "to the first cat and 'youngest' to the last cat."
            ),
            "setup": {"elders": ["Greybeard", "Mittens", "Whiskers", "Pixel"]},
            "hints": [
                "First item: elders[0]",
                "Last item: elders[-1]",
            ],
            "checks": [
                checks.has_var("eldest", "Greybeard"),
                checks.has_var("youngest", "Pixel"),
            ],
            "success": "Both bow their heads.",
        },
        {
            "title": "Shout their names",
            "instructions": (
                "The list 'cats' is set. Create a new list 'shouted' "
                "where every name is UPPERCASE. A for loop or a list "
                "comprehension both work."
            ),
            "setup": {"cats": ["Mittens", "Pixel", "Boots"]},
            "hints": [
                "Loop: shouted = []; for c in cats: shouted.append(c.upper())",
                "Comprehension: shouted = [c.upper() for c in cats]",
            ],
            "checks": [
                checks.has_var("shouted", ["MITTENS", "PIXEL", "BOOTS"]),
            ],
            "success": "The council ROARS Pixel's name. Goosebumps!",
        },
    ],
    "ending": (
        "The eldest cat presses a paw to Pixel's forehead. 'You are ready "
        "for the last lesson. Home is one trick away.'"
    ),
}


CHAPTER_6 = {
    "id": "ch6_tricks",
    "title": "Chapter 6 — Teaching Tricks",
    "cat_mood": "happy",
    "story": (
        "Pixel reaches the edge of the Whisker Woods. A great door "
        "stands shut, guarded by a sleepy door-cat.\n\n"
        "'To go home,' the door-cat yawns, 'teach me three tricks. "
        "Define them as FUNCTIONS, and I shall let you pass.'"
    ),
    "lesson": (
        "A function is a reusable trick you teach Python. You define it "
        "with 'def', give it parameters (inputs), and use 'return' to "
        "send back a result."
    ),
    "example": (
        'def double(x):\n'
        '    return x * 2\n'
        '\n'
        '# Use it:\n'
        'result = double(5)    # result is 10\n'
        '\n'
        'def greet(name):\n'
        '    return f"Hello, {name}!"\n'
        '\n'
        'greet("Pixel")        # "Hello, Pixel!"'
    ),
    "challenges": [
        {
            "title": "The Meow Trick",
            "instructions": (
                "Define a function called 'meow' that takes one parameter "
                "'times' (a number) and returns the string \"meow\" "
                "repeated that many times, separated by single spaces.\n"
                "  meow(1) -> \"meow\"\n"
                "  meow(3) -> \"meow meow meow\""
            ),
            "hints": [
                "\"meow \" * times gives \"meow meow meow \" — note the trailing space.",
                "Use .strip() to remove the trailing space, or join a list.",
                "return (\"meow \" * times).strip()",
            ],
            "checks": [
                checks.func_returns("meow", [
                    ((1,), "meow"),
                    ((3,), "meow meow meow"),
                    ((0,), ""),
                ]),
            ],
            "success": "The door-cat purrs. 'A respectable meow.'",
        },
        {
            "title": "The Hunger Trick",
            "instructions": (
                "Define a function 'is_hungry' that takes one parameter "
                "'treats_eaten' and returns True if treats_eaten is 0, "
                "False otherwise."
            ),
            "hints": [
                "return treats_eaten == 0",
            ],
            "checks": [
                checks.func_returns("is_hungry", [
                    ((0,), True),
                    ((1,), False),
                    ((99,), False),
                ]),
            ],
            "success": "The door-cat's stomach rumbles in sympathy.",
        },
        {
            "title": "The Greeting Trick",
            "instructions": (
                "Define a function 'greet' that takes a name and returns "
                "the string \"Hello, NAME!\" — using f-strings or "
                "concatenation. Example: greet(\"Pixel\") -> "
                "\"Hello, Pixel!\""
            ),
            "hints": [
                "Use an f-string: return f\"Hello, {name}!\"",
                "Don't forget the exclamation mark.",
            ],
            "checks": [
                checks.func_returns("greet", [
                    (("Pixel",), "Hello, Pixel!"),
                    (("Sage",), "Hello, Sage!"),
                    (("",), "Hello, !"),
                ]),
            ],
            "success": "The door-cat bows deeply. 'You may pass, code-cat.'",
        },
    ],
    "ending": (
        "The great door swings open. Beyond it, Pixel sees a familiar "
        "window — and a warm sunbeam on a familiar windowsill. Home.\n\n"
        "Pixel turns back to the Whisker Woods and bows. The forest "
        "whispers, 'Come back any time, code-cat. There is always more "
        "to learn.'"
    ),
}


CHAPTERS = [
    CHAPTER_1,
    CHAPTER_2,
    CHAPTER_3,
    CHAPTER_4,
    CHAPTER_5,
    CHAPTER_6,
]
