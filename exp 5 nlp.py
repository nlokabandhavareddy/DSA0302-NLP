# Porter Stemmer Algorithm using NLTK

from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = [
    "playing",
    "played",
    "playing",
    "running",
    "runner",
    "studies",
    "studying",
    "happiness",
    "connected",
    "connection"
]

print("Original Word\t\tStemmed Word")
print("-" * 35)

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")
