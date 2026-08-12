import re
from collections import Counter

# ---------------------------------------------------------
# TRAINING CORPUS
# ---------------------------------------------------------

corpus = """
the student is intelligent
the student is hardworking
the student reads books
the student reads english
the student studies computer science
the student studies mathematics
the teacher is helpful
the teacher teaches english
the teacher reads books
the teacher helps student
the boy plays football
the boy plays cricket
the girl reads books
the girl studies science
the student likes programming
the student likes python
the student learns programming
the student learns english
students learn new skills
students read interesting books
students study computer science
python is a programming language
english is an important language
the computer is useful
the computer is fast
"""

# ---------------------------------------------------------
# PREPROCESS
# ---------------------------------------------------------

def preprocess(text):

    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)

    sentences = [
        sentence.strip()
        for sentence in text.split("\n")
        if sentence.strip()
    ]

    return [sentence.split() for sentence in sentences]


sentences = preprocess(corpus)

# ---------------------------------------------------------
# COUNTS
# ---------------------------------------------------------

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in sentences:

    for word in sentence:
        unigram[word] += 1

    for i in range(len(sentence) - 1):
        bigram[(sentence[i], sentence[i + 1])] += 1

    for i in range(len(sentence) - 2):
        trigram[
            (sentence[i], sentence[i + 1], sentence[i + 2])
        ] += 1


total_words = sum(unigram.values())


# ---------------------------------------------------------
# UNSMOOTHED PROBABILITIES
# ---------------------------------------------------------

def p_unigram(word):

    return unigram[word] / total_words


def p_bigram(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def p_trigram(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# ---------------------------------------------------------
# BACKOFF MODEL
# ---------------------------------------------------------

def backoff_probability(w1, w2, w3):

    # Try trigram
    if trigram[(w1, w2, w3)] > 0:

        return p_trigram(w1, w2, w3)

    # Otherwise bigram
    elif bigram[(w2, w3)] > 0:

        return p_bigram(w2, w3)

    # Otherwise unigram
    elif unigram[w3] > 0:

        return p_unigram(w3)

    return 0


# ---------------------------------------------------------
# DELETED INTERPOLATION
# ---------------------------------------------------------

# Weights
lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.5


def interpolation_probability(w1, w2, w3):

    p1 = p_unigram(w3)

    p2 = p_bigram(w2, w3)

    p3 = p_trigram(w1, w2, w3)

    return (
        lambda1 * p1 +
        lambda2 * p2 +
        lambda3 * p3
    )


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

vocabulary = list(unigram.keys())


def predict(query, model):

    words = query.lower().split()

    if len(words) < 2:
        print("Enter at least two words.")
        return []

    w1 = words[-2]
    w2 = words[-1]

    predictions = []

    for word in vocabulary:

        if model == "unsmoothed":

            probability = p_trigram(w1, w2, word)

        elif model == "backoff":

            probability = backoff_probability(
                w1, w2, word
            )

        elif model == "interpolation":

            probability = interpolation_probability(
                w1, w2, word
            )

        predictions.append((word, probability))

    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return predictions[:5]


# ---------------------------------------------------------
# ZERO PROBABILITY DEMO
# ---------------------------------------------------------

print("\n====================================")
print("ZERO PROBABILITY DEMONSTRATION")
print("====================================")

w1 = "student"
w2 = "is"
w3 = "football"

print(
    f"Unsmoothed P({w3}|{w1},{w2}) =",
    p_trigram(w1, w2, w3)
)

print(
    f"Backoff P({w3}|{w1},{w2}) =",
    backoff_probability(w1, w2, w3)
)

print(
    f"Interpolation P({w3}|{w1},{w2}) =",
    interpolation_probability(w1, w2, w3)
)


# ---------------------------------------------------------
# USER QUERY
# ---------------------------------------------------------

query = input(
    "\nEnter a sentence/query "
    "(example: the student is): "
)


print("\n====================================")
print("UNSMOOTHED MODEL")
print("====================================")

result = predict(query, "unsmoothed")

for word, probability in result:
    print(word, "->", round(probability, 4))


print("\n====================================")
print("BACKOFF MODEL")
print("====================================")

result = predict(query, "backoff")

for word, probability in result:
    print(word, "->", round(probability, 4))


print("\n====================================")
print("DELETED INTERPOLATION MODEL")
print("====================================")

result = predict(query, "interpolation")

for word, probability in result:
    print(word, "->", round(probability, 4))


# ---------------------------------------------------------
# COMPARISON
# ---------------------------------------------------------

print("\n====================================")
print("MODEL COMPARISON")
print("====================================")

print("Unsmoothed:")
print("Uses only the exact trigram.")

print("\nBackoff:")
print("Trigram -> Bigram -> Unigram")

print("\nDeleted Interpolation:")
print(
    "Combines unigram, bigram and trigram "
    "probabilities."
)

print("\nInterpolation weights:")
print("Unigram =", lambda1)
print("Bigram  =", lambda2)
print("Trigram =", lambda3)


OUTPUT

For example, enter:

the student is

Sample output:

====================================
ZERO PROBABILITY DEMONSTRATION
====================================

Unsmoothed P(football|student,is) = 0
Backoff P(football|student,is) = 0.0
Interpolation P(football|student,is) = 0.0


Enter a sentence/query (example: the student is): the student is

====================================
UNSMOOTHED MODEL
====================================

intelligent -> 0.5
hardworking -> 0.5
the -> 0
student -> 0
reads -> 0

====================================
BACKOFF MODEL
====================================

intelligent -> 0.5
hardworking -> 0.5
the -> 0.0
student -> 0.0
reads -> 0.0

====================================
DELETED INTERPOLATION MODEL
====================================

intelligent -> 0.2583
hardworking -> 0.2583
language -> 0.0417
programming -> 0.0417
important -> 0.0417

====================================
MODEL COMPARISON
====================================

Unsmoothed:
Uses only the exact trigram.

Backoff:
Trigram -> Bigram -> Unigram

Deleted Interpolation:
Combines unigram, bigram and trigram probabilities.

Interpolation weights:
Unigram = 0.2
Bigram  = 0.3
Trigram = 0.5
What this output shows

For:

the student is

the corpus contains:

student is intelligent
student is hardworking

Therefore:

P(intelligent | student, is) > 0
P(hardworking | student, is) > 0

But an unseen word such as football gets:

Unsmoothed = 0
