# Morphological Parser

words = ["disagree", "agreement", "agreeable"]

print("{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Category", "Meaning"))

for word in words:

    prefix = "-"
    suffix = "-"

    if word.startswith("dis"):
        prefix = "dis"
        root = "agree"
        category = "Derivational"
        meaning = "Negative"

    elif word.endswith("ment"):
        root = "agree"
        suffix = "ment"
        category = "Derivational"
        meaning = "Action"

    elif word.endswith("able"):
        root = "agree"
        suffix = "able"
        category = "Derivational"
        meaning = "Capability"

    print("{:<15}{:<10}{:<10}{:<10}{:<15}{:<15}".format(
        word, prefix, root, suffix, category, meaning))

#OUTPUT
    Word           Prefix    Root      Suffix    Category       Meaning        
disagree       dis       agree     -         Derivational   Negative       
agreement      -         agree     ment      Derivational   Action         
agreeable      -         agree     able      Derivational   Capability     


