# Rule-Based Morphological Processing

words = ["analyzing", "analysis", "analytical"]

print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
    "Original", "Root", "Affix", "Type", "Normalized"))

for word in words:
    root = "analyze"

    if word.endswith("ing"):
        affix = "ing"
        mtype = "Inflectional"

    elif word.endswith("sis"):
        affix = "sis"
        mtype = "Derivational"

    elif word.endswith("ical"):
        affix = "ical"
        mtype = "Derivational"

    else:
        affix = "-"
        mtype = "Base"

    print("{:<15}{:<12}{:<10}{:<15}{:<12}".format(
        word, root, affix, mtype, root))
#OUTPUT
    Original       Root        Affix     Type           Normalized  
analyzing      analyze     ing       Inflectional   analyze     
analysis       analyze     sis       Derivational   analyze     
analytical     analyze     ical      Derivational   analyze  
