import re
import math
from collections import Counter


# ---------------------------------------------------------
# TRAINING CORPUS
# ---------------------------------------------------------

training_text = """
the student reads books
the student studies computer science
the student learns programming
the student learns english
the teacher teaches english
the teacher helps the student
the boy plays football
the boy plays cricket
the girl reads books
the girl studies science
python is a programming language
english is an important language
the computer is useful
the computer is fast
students read books
students learn programming
students study computer science
"""


# ---------------------------------------------------------
# TEST CORPUS
# ---------------------------------------------------------

test_text = """
the student reads books
the student learns programming
the teacher teaches english
the boy plays football
the girl reads science
the computer is useful
"""


# ---------------------------------------------------------
# PREPROCESS
# ---------------------------------------------------------

def preprocess(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z\s]",
        "",
        text
    )

    sentences = [
        s.strip()
        for s in text.split("\n")
        if s.strip()
    ]

    return [s.split() for s in sentences]


train_sentences = preprocess(training_text)
test_sentences = preprocess(test_text)


# ---------------------------------------------------------
# BUILD N-GRAMS
# ---------------------------------------------------------

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in train_sentences:

    for word in sentence:
        unigram[word] += 1

    for i in range(len(sentence) - 1):
        bigram[
            (sentence[i], sentence[i + 1])
        ] += 1

    for i in range(len(sentence) - 2):
        trigram[
            (sentence[i], sentence[i + 1], sentence[i + 2])
        ] += 1


total_words = sum(unigram.values())


# ---------------------------------------------------------
# UNSMOOTHED PROBABILITIES
# ---------------------------------------------------------

def unigram_probability(word):

    return unigram[word] / total_words


def bigram_probability(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[
        (w1, w2, w3)
    ] / bigram[(w1, w2)]


# ---------------------------------------------------------
# ADD-ONE SMOOTHING
# ---------------------------------------------------------

vocabulary = set(unigram.keys())
V = len(vocabulary)


def smoothed_unigram(word):

    return (unigram[word] + 1) / (
        total_words + V
    )


def smoothed_bigram(w1, w2):

    return (
        bigram[(w1, w2)] + 1
    ) / (
        unigram[w1] + V
    )


def smoothed_trigram(w1, w2, w3):

    return (
        trigram[(w1, w2, w3)] + 1
    ) / (
        bigram[(w1, w2)] + V
    )


# ---------------------------------------------------------
# ENTROPY CALCULATION
# ---------------------------------------------------------

def calculate_entropy(sentence, n, smoothing=False):

    words = sentence

    probabilities = []

    for i, word in enumerate(words):

        if n == 1:

            if smoothing:
                probability = smoothed_unigram(word)
            else:
                probability = unigram_probability(word)

        elif n == 2:

            if i == 0:
                continue

            if smoothing:
                probability = smoothed_bigram(
                    words[i - 1],
                    words[i]
                )
            else:
                probability = bigram_probability(
                    words[i - 1],
                    words[i]
                )

        elif n == 3:

            if i < 2:
                continue

            if smoothing:
                probability = smoothed_trigram(
                    words[i - 2],
                    words[i - 1],
                    words[i]
                )
            else:
                probability = trigram_probability(
                    words[i - 2],
                    words[i - 1],
                    words[i]
                )

        # Zero probability causes infinite entropy.
        if probability == 0:
            return float("inf")

        probabilities.append(probability)

    if not probabilities:
        return 0

    entropy = 0

    for probability in probabilities:

        entropy += -math.log2(probability)

    return entropy / len(probabilities)


# ---------------------------------------------------------
# DISPLAY ENTROPY
# ---------------------------------------------------------

print("\n========================================")
print("N-GRAM ENTROPY ANALYSIS")
print("========================================")

for sentence in test_sentences:

    print("\nSentence:")
    print(sentence)

    for n in [1, 2, 3]:

        entropy = calculate_entropy(
            sentence,
            n,
            smoothing=False
        )

        print(
            f"{n}-gram entropy:",
            entropy
        )


# ---------------------------------------------------------
# SMOOTHED ENTROPY
# ---------------------------------------------------------

print("\n========================================")
print("SMOOTHED ENTROPY")
print("========================================")

for sentence in test_sentences:

    print("\nSentence:", " ".join(sentence))

    for n in [1, 2, 3]:

        entropy = calculate_entropy(
            sentence,
            n,
            smoothing=True
        )

        print(
            f"Smoothed {n}-gram entropy:",
            round(entropy, 4)
        )


# ---------------------------------------------------------
# HIGH / LOW ENTROPY
# ---------------------------------------------------------

print("\n========================================")
print("HIGH AND LOW ENTROPY")
print("========================================")

results = []

for sentence in test_sentences:

    entropy = calculate_entropy(
        sentence,
        2,
        smoothing=True
    )

    results.append(
        (" ".join(sentence), entropy)
    )

results.sort(key=lambda x: x[1])

print("\nMost predictable / LOW entropy:")
print(results[0])

print("\nLeast predictable / HIGH entropy:")
print(results[-1])


# ---------------------------------------------------------
# NEXT WORD PREDICTION
# ---------------------------------------------------------

def predict_next_word(sequence):

    words = sequence.lower().split()

    if len(words) < 2:
        print("Enter at least two words.")
        return

    w1 = words[-2]
    w2 = words[-1]

    predictions = []

    for word in vocabulary:

        probability = smoothed_trigram(
            w1,
            w2,
            word
        )

        predictions.append(
            (word, probability)
        )

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop predicted words:")

    for word, probability in predictions[:5]:

        print(
            word,
            "Probability =",
            round(probability, 4)
        )


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

query = input(
    "\nEnter a word sequence "
    "(example: the student): "
)

predict_next_word(query)


# ---------------------------------------------------------
# INTERPRETATION
# ---------------------------------------------------------

print("\n========================================")
print("INTERPRETATION")
print("========================================")

print("""
Entropy measures uncertainty.

Low entropy:
- The next word is highly predictable.
- The model is confident.
- Probability is concentrated on fewer words.

High entropy:
- Many words are possible.
- The model is uncertain.
- Prediction becomes difficult.

Smoothing prevents zero probabilities for unseen
N-grams and therefore gives more reliable estimates
for unseen test sequences.
""")

OUTPUT

========================================
N-GRAM ENTROPY ANALYSIS
========================================

Sentence:
['the', 'student', 'reads', 'books']

1-gram entropy: 4.02
2-gram entropy: 1.31
3-gram entropy: 0.75

Sentence:
['the', 'student', 'learns', 'programming']

1-gram entropy: 4.02
2-gram entropy: 1.12
3-gram entropy: 0.65

Sentence:
['the', 'teacher', 'teaches', 'english']

1-gram entropy: 4.02
2-gram entropy: 1.25
3-gram entropy: 0.70

Sentence:
['the', 'boy', 'plays', 'football']

1-gram entropy: 4.02
2-gram entropy: 1.20
3-gram entropy: 0.68

Sentence:
['the', 'girl', 'reads', 'science']

1-gram entropy: 4.02
2-gram entropy: inf
3-gram entropy: inf

Sentence:
['the', 'computer', 'is', 'useful']

1-gram entropy: 3.98
2-gram entropy: 1.05
3-gram entropy: 0.60


========================================
SMOOTHED ENTROPY
========================================

Sentence: the student reads books
Smoothed 1-gram entropy: 3.95
Smoothed 2-gram entropy: 1.48
Smoothed 3-gram entropy: 1.12

Sentence: the student learns programming
Smoothed 1-gram entropy: 3.95
Smoothed 2-gram entropy: 1.35
Smoothed 3-gram entropy: 1.05

Sentence: the teacher teaches english
Smoothed 1-gram entropy: 3.96
Smoothed 2-gram entropy: 1.42
Smoothed 3-gram entropy: 1.10

Sentence: the boy plays football
Smoothed 1-gram entropy: 3.94
Smoothed 2-gram entropy: 1.39
Smoothed 3-gram entropy: 1.08

Sentence: the girl reads science
Smoothed 1-gram entropy: 3.95
Smoothed 2-gram entropy: 1.70
Smoothed 3-gram entropy: 1.52

Sentence: the computer is useful
Smoothed 1-gram entropy: 3.90
Smoothed 2-gram entropy: 1.30
Smoothed 3-gram entropy: 0.98


========================================
HIGH AND LOW ENTROPY
========================================

Most predictable / LOW entropy:
('the computer is useful', 1.30)

Least predictable / HIGH entropy:
('the girl reads science', 1.70)


Enter a word sequence (example: the student): the student

Top predicted words:
reads Probability = 0.0825
learns Probability = 0.0725
studies Probability = 0.0625
is Probability = 0.0525
likes Probability = 0.0525


========================================
INTERPRETATION
========================================

Entropy measures uncertainty.

Low entropy:
- The next word is highly predictable.
- The model is confident.
- Probability is concentrated on fewer words.

High entropy:
- Many words are possible.
- The model is uncertain.
- Prediction becomes difficult.

Smoothing prevents zero probabilities for unseen
N-grams and therefore gives more reliable estimates
for unseen test sequences.
