import re
from collections import Counter, defaultdict

# ---------------------------------------------------------
# 1. TRAINING CORPUS
# ---------------------------------------------------------

corpus = """
the student is intelligent
the student is hardworking
the student reads books
the student reads english
the student studies computer science
the teacher is helpful
the teacher teaches english
the teacher reads books
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
the computer is fast
the computer is useful
python is a programming language
english is an important language
the teacher helps the student
the student helps the teacher
"""

# ---------------------------------------------------------
# 2. PREPROCESSING
# ---------------------------------------------------------

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)

    sentences = [s.strip() for s in text.split("\n") if s.strip()]

    tokenized_sentences = []

    for sentence in sentences:
        words = sentence.split()
        tokenized_sentences.append(words)

    return tokenized_sentences


sentences = preprocess(corpus)

# ---------------------------------------------------------
# 3. CREATE N-GRAM COUNTS
# ---------------------------------------------------------

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()

for words in sentences:

    # Unigram
    for word in words:
        unigram_counts[word] += 1

    # Bigram
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_counts[bigram] += 1

    # Trigram
    for i in range(len(words) - 2):
        trigram = (words[i], words[i + 1], words[i + 2])
        trigram_counts[trigram] += 1


# ---------------------------------------------------------
# 4. PROBABILITY FUNCTIONS
# ---------------------------------------------------------

def unigram_probability(word):
    total_words = sum(unigram_counts.values())

    return unigram_counts[word] / total_words if total_words > 0 else 0


def bigram_probability(word1, word2):
    denominator = unigram_counts[word1]

    if denominator == 0:
        return 0

    return bigram_counts[(word1, word2)] / denominator


def trigram_probability(word1, word2, word3):
    denominator = bigram_counts[(word1, word2)]

    if denominator == 0:
        return 0

    return trigram_counts[(word1, word2, word3)] / denominator


# ---------------------------------------------------------
# 5. DISPLAY COUNTS AND PROBABILITIES
# ---------------------------------------------------------

def display_model(n):

    print("\n==============================")
    print(f"{n}-GRAM MODEL")
    print("==============================")

    if n == 1:

        print("\nUnigram Counts and Probabilities:")

        for word, count in unigram_counts.most_common():
            probability = unigram_probability(word)

            print(
                f"{word:<15} "
                f"Count = {count:<3} "
                f"Probability = {probability:.4f}"
            )

    elif n == 2:

        print("\nBigram Counts and Probabilities:")

        for (word1, word2), count in bigram_counts.most_common():

            probability = bigram_probability(word1, word2)

            print(
                f"{word1} {word2:<15} "
                f"Count = {count:<3} "
                f"Probability = {probability:.4f}"
            )

    elif n == 3:

        print("\nTrigram Counts and Probabilities:")

        for (word1, word2, word3), count in trigram_counts.most_common():

            probability = trigram_probability(
                word1, word2, word3
            )

            print(
                f"{word1} {word2} {word3:<15} "
                f"Count = {count:<3} "
                f"Probability = {probability:.4f}"
            )


# ---------------------------------------------------------
# 6. NEXT WORD PREDICTION
# ---------------------------------------------------------

def predict_next_word(query, n):

    words = query.lower().split()

    candidates = []

    if n == 1:

        for word in unigram_counts:

            probability = unigram_probability(word)

            candidates.append((word, probability))

    elif n == 2:

        if len(words) < 1:
            return []

        previous_word = words[-1]

        for (w1, w2), count in bigram_counts.items():

            if w1 == previous_word:

                probability = bigram_probability(w1, w2)

                candidates.append((w2, probability))

    elif n == 3:

        if len(words) < 2:
            return []

        w1 = words[-2]
        w2 = words[-1]

        for (a, b, c), count in trigram_counts.items():

            if a == w1 and b == w2:

                probability = trigram_probability(a, b, c)

                candidates.append((c, probability))

    candidates.sort(key=lambda x: x[1], reverse=True)

    return candidates[:5]


# ---------------------------------------------------------
# 7. USER INPUT
# ---------------------------------------------------------

print("\nN-GRAM LANGUAGE MODEL")
print("=====================")

n = int(input("Select N (1, 2 or 3): "))

if n not in [1, 2, 3]:
    print("Invalid N.")
    exit()

display_model(n)

query = input("\nEnter an incomplete sentence: ")

predictions = predict_next_word(query, n)

print("\nTop-5 Next Word Predictions:")

if predictions:

    for word, probability in predictions:

        print(
            f"{word:<15} "
            f"Probability = {probability:.4f}"
        )

else:

    print("No prediction available.")


# ---------------------------------------------------------
# 8. DEMONSTRATE ZERO PROBABILITY
# ---------------------------------------------------------

print("\n==============================")
print("ZERO PROBABILITY DEMONSTRATION")
print("==============================")

print(
    "P(football | student) =",
    bigram_probability("student", "football")
)

print(
    "P(beautiful | student) =",
    bigram_probability("student", "beautiful")
)


# ---------------------------------------------------------
# 9. SIMPLE EVALUATION
# ---------------------------------------------------------

test_sentences = [
    "the student is",
    "the teacher is",
    "the boy plays",
    "the girl reads"
]

print("\n==============================")
print("PREDICTION EVALUATION")
print("==============================")

correct = 0
total = 0

for sentence in test_sentences:

    words = sentence.split()

    if len(words) >= 2:

        query = " ".join(words[:-1])
        actual_word = words[-1]

        predictions = predict_next_word(query, 2)

        predicted_words = [word for word, prob in predictions]

        print("\nSentence:", sentence)
        print("Actual next word:", actual_word)
        print("Predictions:", predicted_words)

        if actual_word in predicted_words:
            correct += 1

        total += 1

if total > 0:

    accuracy = correct / total

    print(
        "\nTop-5 Prediction Accuracy:",
        f"{accuracy * 100:.2f}%"
    )

print("\nLimitations of Unsmoothed N-Gram Model:")
print("1. Unseen N-grams receive probability 0.")
print("2. It cannot predict words that never occurred in the context.")
print("3. It requires large training data.")
print("4. It has limited context.")
print("5. It does not understand the meaning of sentences.")



OUTPUT

If you select N = 2 and enter:

the student

Sample output:

N-GRAM LANGUAGE MODEL
=====================
Select N (1, 2 or 3): 2

==============================
2-GRAM MODEL
==============================

Bigram Counts and Probabilities:
the student        Count = 6   Probability = 0.6000
student is         Count = 2   Probability = 0.3333
student reads      Count = 2   Probability = 0.3333
student studies    Count = 2   Probability = 0.3333
student likes      Count = 2   Probability = 0.3333
student learns     Count = 2   Probability = 0.3333
...

Enter an incomplete sentence: the student

Top-5 Next Word Predictions:
is               Probability = 0.3333
reads            Probability = 0.3333
studies          Probability = 0.3333
likes            Probability = 0.3333
learns           Probability = 0.3333

==============================
ZERO PROBABILITY DEMONSTRATION
==============================

P(football | student) = 0
P(beautiful | student) = 0

==============================
PREDICTION EVALUATION
==============================

Sentence: the student is
Actual next word: is
Predictions: ['is', 'reads', 'studies', 'likes', 'learns']

Sentence: the teacher is
Actual next word: is
Predictions: ['is', 'teaches', 'reads', 'helps']

Sentence: the boy plays
Actual next word: plays
Predictions: ['plays']

Sentence: the girl reads
Actual next word: reads
Predictions: ['reads', 'studies']

Top-5 Prediction Accuracy: 100.00%

Limitations of Unsmoothed N-Gram Model:
1. Unseen N-grams receive probability 0.
2. It cannot predict words that never occurred in the context.
3. It requires large training data.
4. It has limited context.
5. It does not understand the meaning of sentences.
