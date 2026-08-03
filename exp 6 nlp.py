# Basic Bigram Model for Text Generation

import random
from collections import defaultdict

# Sample text corpus
text = """
Python is a popular programming language.
Python is easy to learn.
Python is widely used for data science and machine learning.
Machine learning is an important field.
"""

# Convert text to lowercase and split into words
words = text.lower().replace(".", "").split()

# Create bigram dictionary
bigram = defaultdict(list)

for i in range(len(words) - 1):
    bigram[words[i]].append(words[i + 1])

# Starting word
current_word = "python"

generated = [current_word]

# Generate 15 words
for _ in range(15):
    if current_word in bigram:
        next_word = random.choice(bigram[current_word])
        generated.append(next_word)
        current_word = next_word
    else:
        break

# Display generated text
print("Generated Text:")
print(" ".join(generated))
