# Finite State Machine for Morphological Parsing
# Generate plural forms of English nouns

def pluralize(noun):
    vowels = "aeiou"

    # Rule 1: Ends with s, x, z, sh, ch
    if noun.endswith(("s", "x", "z", "sh", "ch")):
        return noun + "es"

    # Rule 2: Ends with consonant + y
    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in vowels:
        return noun[:-1] + "ies"

    # Rule 3: Ends with fe
    elif noun.endswith("fe"):
        return noun[:-2] + "ves"

    # Rule 4: Ends with f
    elif noun.endswith("f"):
        return noun[:-1] + "ves"

    # Rule 5: Default
    else:
        return noun + "s"


# Main Program
word = input("Enter a singular noun: ")
plural = pluralize(word)

print("Plural form:", plural)
