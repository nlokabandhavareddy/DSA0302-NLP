# Morphological Analysis using NLTK

from nltk.stem import PorterStemmer

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "playing",
    "played",
    "running",
    "studies",
    "studying",
    "happiness",
    "connected",
    "connection",
    "walking",
    "talked"
]

print("Original Word\tStem Word")
print("-" * 30)

# Perform morphological analysis
for word in words:
    stem = stemmer.stem(word)
    print(f"{word}\t\t{stem}")
