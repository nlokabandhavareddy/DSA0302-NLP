# Part-of-Speech (POS) Tagging using NLTK

import nltk
from nltk.tokenize import word_tokenize

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
text = "Python is a powerful programming language used for artificial intelligence."

# Tokenize the sentence
words = word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Display the result
print("Word\t\tPOS Tag")
print("-" * 30)

for word, tag in pos_tags:
    print(f"{word}\t\t{tag}")
