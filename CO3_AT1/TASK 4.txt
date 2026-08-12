import re
from collections import Counter, defaultdict


# =========================================================
# TRAINING DATA
# =========================================================

training_data = [
    [
        ("the", "DT"),
        ("student", "NN"),
        ("reads", "VBZ"),
        ("books", "NNS")
    ],

    [
        ("the", "DT"),
        ("student", "NN"),
        ("studies", "VBZ"),
        ("english", "NN")
    ],

    [
        ("the", "DT"),
        ("teacher", "NN"),
        ("helps", "VBZ"),
        ("the", "DT"),
        ("student", "NN")
    ],

    [
        ("the", "DT"),
        ("boy", "NN"),
        ("plays", "VBZ"),
        ("football", "NN")
    ],

    [
        ("the", "DT"),
        ("girl", "NN"),
        ("reads", "VBZ"),
        ("books", "NNS")
    ],

    [
        ("the", "DT"),
        ("student", "NN"),
        ("is", "VBZ"),
        ("intelligent", "JJ")
    ],

    [
        ("the", "DT"),
        ("student", "NN"),
        ("learns", "VBZ"),
        ("quickly", "RB")
    ],

    [
        ("i", "PRP"),
        ("read", "VB"),
        ("books", "NNS")
    ],

    [
        ("she", "PRP"),
        ("plays", "VBZ"),
        ("football", "NN")
    ],

    [
        ("he", "PRP"),
        ("is", "VBZ"),
        ("happy", "JJ")
    ],

    [
        ("students", "NNS"),
        ("study", "VB"),
        ("computer", "NN"),
        ("science", "NN")
    ],

    [
        ("the", "DT"),
        ("smart", "JJ"),
        ("student", "NN"),
        ("works", "VBZ"),
        ("quickly", "RB")
    ]
]


# =========================================================
# 1. BUILD STATISTICS
# =========================================================

word_tag_counts = Counter()
tag_counts = Counter()
transition_counts = Counter()

for sentence in training_data:

    previous_tag = "<START>"

    for word, tag in sentence:

        word_tag_counts[(word, tag)] += 1

        tag_counts[tag] += 1

        transition_counts[
            (previous_tag, tag)
        ] += 1

        previous_tag = tag


# =========================================================
# 2. RULE-BASED POS TAGGER
# =========================================================

lexicon = {
    "i": "PRP",
    "you": "PRP",
    "he": "PRP",
    "she": "PRP",
    "we": "PRP",
    "they": "PRP",

    "the": "DT",
    "a": "DT",
    "an": "DT",

    "and": "CC",
    "but": "CC",
    "or": "CC",

    "in": "IN",
    "on": "IN",
    "at": "IN",
    "with": "IN",
    "from": "IN",
    "to": "IN",

    "is": "VBZ",
    "am": "VBP",
    "are": "VBP",

    "student": "NN",
    "teacher": "NN",
    "boy": "NN",
    "girl": "NN",
    "book": "NN",
    "books": "NNS",
    "football": "NN",
    "computer": "NN",
    "science": "NN",

    "happy": "JJ",
    "smart": "JJ",
    "intelligent": "JJ",
    "important": "JJ",

    "quickly": "RB",

    "read": "VB",
    "study": "VB",
    "learn": "VB",

    "reads": "VBZ",
    "studies": "VBZ",
    "learns": "VBZ",
    "plays": "VBZ",
    "helps": "VBZ",
    "works": "VBZ"
}


def rule_based_tagger(words):

    tags = []

    for word in words:

        word_lower = word.lower()

        # Dictionary lookup
        if word_lower in lexicon:

            tag = lexicon[word_lower]

        # Adverb
        elif word_lower.endswith("ly"):

            tag = "RB"

        # Gerund
        elif word_lower.endswith("ing"):

            tag = "VBG"

        # Past tense
        elif word_lower.endswith("ed"):

            tag = "VBD"

        # Adjective
        elif word_lower.endswith(
            ("ous", "ful", "able", "ive", "al")
        ):

            tag = "JJ"

        # Plural noun
        elif word_lower.endswith("s"):

            tag = "NNS"

        # Default
        else:

            tag = "NN"

        tags.append(tag)

    return list(zip(words, tags))


# =========================================================
# 3. STOCHASTIC POS TAGGER
# =========================================================

all_tags = list(tag_counts.keys())


def emission_probability(word, tag):

    count = word_tag_counts[(word, tag)]

    total = sum(
        word_tag_counts[(word, t)]
        for t in all_tags
    )

    if total == 0:
        return 1e-6

    return count / total if count > 0 else 1e-6


def transition_probability(previous_tag, current_tag):

    count = transition_counts[
        (previous_tag, current_tag)
    ]

    total = sum(
        transition_counts[
            (previous_tag, tag)
        ]
        for tag in all_tags
    )

    if total == 0:
        return 1e-6

    return count / total if count > 0 else 1e-6


def stochastic_tagger(words):

    result = []

    previous_tag = "<START>"

    for word in words:

        word = word.lower()

        best_tag = None
        best_score = -1

        for tag in all_tags:

            emission = emission_probability(
                word,
                tag
            )

            transition = transition_probability(
                previous_tag,
                tag
            )

            score = emission * transition

            if score > best_score:

                best_score = score
                best_tag = tag

        result.append(
            (word, best_tag)
        )

        previous_tag = best_tag

    return result


# =========================================================
# 4. TRANSFORMATION-BASED TAGGING
# =========================================================

def transformation_based_tagger(words):

    # Initial tagging
    tagged = rule_based_tagger(words)

    corrected = []

    for i, (word, tag) in enumerate(tagged):

        new_tag = tag

        # Rule 1:
        # Pronoun + noun-like word -> Verb
        if i > 0:

            previous_word, previous_tag = tagged[i - 1]

            if previous_tag == "PRP":

                if word.lower().endswith(
                    ("s", "ed", "ing")
                ):

                    new_tag = "VBZ"

        # Rule 2:
        # Auxiliary verb + adjective
        if i > 0:

            previous_word, previous_tag = tagged[i - 1]

            if previous_word.lower() in [
                "is",
                "am",
                "are"
            ]:

                if word.lower() in [
                    "happy",
                    "smart",
                    "intelligent",
                    "important"
                ]:

                    new_tag = "JJ"

        # Rule 3:
        # Words ending in -ly -> adverb
        if word.lower().endswith("ly"):

            new_tag = "RB"

        # Rule 4:
        # Words ending in -ing -> VBG
        if word.lower().endswith("ing"):

            new_tag = "VBG"

        # Rule 5:
        # Words ending in -ed -> VBD
        if word.lower().endswith("ed"):

            new_tag = "VBD"

        corrected.append(
            (word, new_tag)
        )

    return corrected


# =========================================================
# 5. DISPLAY FUNCTION
# =========================================================

def display(title, tagged):

    print("\n" + "=" * 50)

    print(title)

    print("=" * 50)

    for word, tag in tagged:

        print(
            f"{word:<15} -> {tag}"
        )


# =========================================================
# 6. USER INPUT
# =========================================================

sentence = input(
    "\nEnter an English sentence: "
)

words = re.findall(
    r"[A-Za-z]+",
    sentence
)


# =========================================================
# 7. APPLY THREE TAGGERS
# =========================================================

rule_result = rule_based_tagger(words)

stochastic_result = stochastic_tagger(words)

transformation_result = transformation_based_tagger(words)


# =========================================================
# 8. DISPLAY RESULTS
# =========================================================

display(
    "RULE-BASED POS TAGGER",
    rule_result
)

display(
    "STOCHASTIC POS TAGGER",
    stochastic_result
)

display(
    "TRANSFORMATION-BASED POS TAGGER",
    transformation_result
)


# =========================================================
# 9. COMPARISON
# =========================================================

print("\n" + "=" * 50)
print("COMPARISON")
print("=" * 50)

print("""
Rule-Based Tagger:
- Uses dictionaries and grammar rules.
- Easy to understand.
- Works well for known words.
- Can fail for ambiguous words.

Stochastic Tagger:
- Uses probabilities from training data.
- Handles ambiguity better.
- Requires training data.
- Can fail for unseen words.

Transformation-Based Tagger:
- Starts with initial tags.
- Applies correction rules.
- Improves incorrect initial tags.
- Combines simple rules with contextual information.

For a small controlled corpus, the stochastic or
transformation-based approach generally performs better
than a simple rule-based approach.
""")


# =========================================================
# 10. PENN TREEBANK TAGSET
# =========================================================

print("\n" + "=" * 50)
print("PENN TREEBANK TAGSET USED")
print("=" * 50)

tagset = {
    "NN": "Noun, singular",
    "NNS": "Noun, plural",
    "VB": "Verb, base form",
    "VBD": "Verb, past tense",
    "VBG": "Verb, gerund/present participle",
    "VBZ": "Verb, 3rd person singular",
    "JJ": "Adjective",
    "RB": "Adverb",
    "PRP": "Personal pronoun",
    "DT": "Determiner",
    "IN": "Preposition",
    "CC": "Coordinating conjunction"
}

for tag, meaning in tagset.items():

    print(
        f"{tag:<5} -> {meaning}"
    )

OUTPUT

For input:

The smart student works quickly

Sample output:

Enter an English sentence: The smart student works quickly

==================================================
RULE-BASED POS TAGGER
==================================================

The             -> DT
smart           -> JJ
student         -> NN
works           -> VBZ
quickly         -> RB


==================================================
STOCHASTIC POS TAGGER
==================================================

the             -> DT
smart           -> JJ
student         -> NN
works           -> VBZ
quickly         -> RB


==================================================
TRANSFORMATION-BASED POS TAGGER
==================================================

The             -> DT
smart           -> JJ
student         -> NN
works           -> VBZ
quickly         -> RB


==================================================
COMPARISON
==================================================

Rule-Based Tagger:
- Uses dictionaries and grammar rules.
- Easy to understand.
- Works well for known words.
- Can fail for ambiguous words.

Stochastic Tagger:
- Uses probabilities from training data.
- Handles ambiguity better.
- Requires training data.
- Can fail for unseen words.

Transformation-Based Tagger:
- Starts with initial tags.
- Applies correction rules.
- Improves incorrect initial tags.
- Combines simple rules with contextual information.

For a small controlled corpus, the stochastic or
transformation-based approach generally performs better
than a simple rule-based approach.


==================================================
PENN TREEBANK TAGSET USED
==================================================

NN    -> Noun, singular
NNS   -> Noun, plural
VB    -> Verb, base form
VBD   -> Verb, past tense
VBG   -> Verb, gerund/present participle
VBZ   -> Verb, 3rd person singular
JJ    -> Adjective
RB    -> Adverb
PRP   -> Personal pronoun
DT    -> Determiner
IN    -> Preposition
CC    -> Coordinating conjunction
Another useful test

Input:

She plays football

Output:

==================================================
RULE-BASED POS TAGGER
==================================================

She             -> PRP
plays           -> VBZ
football        -> NN


==================================================
STOCHASTIC POS TAGGER
==================================================

she             -> PRP
plays           -> VBZ
football        -> NN


==================================================
TRANSFORMATION-BASED POS TAGGER
==================================================

She             -> PRP
plays           -> VBZ
football        -> NN

O
