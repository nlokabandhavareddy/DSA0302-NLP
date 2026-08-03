# Regular Expressions in Python

import re

# Sample text
text = "My name is John. My phone number is 9876543210."

# Search for the word "John"
result = re.search(r"John", text)

if result:
    print("Word found:", result.group())
else:
    print("Word not found")

# Find all words starting with 'M'
words = re.findall(r"\bM\w+", text)
print("Words starting with 'M':", words)

# Match at the beginning of the string
start = re.match(r"My", text)

if start:
    print("Text starts with 'My'")
else:
    print("Text does not start with 'My'")
