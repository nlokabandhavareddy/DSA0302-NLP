# Morphology-Based Normalization

words = ["govern", "government", "governance"]

print("{:<15}{:<12}{:<10}{:<12}{:<12}".format(
    "Word", "Root", "Suffix", "Level", "Normalized"))

for word in words:

    if word == "govern":
        root = "govern"
        suffix = "-"
        level = "Base"

    elif word.endswith("ment"):
        root = "govern"
        suffix = "ment"
        level = "Level-1"

    elif word.endswith("ance"):
        root = "govern"
        suffix = "ance"
        level = "Level-1"

    print("{:<15}{:<12}{:<10}{:<12}{:<12}".format(
        word, root, suffix, level, root))
#OUTPUT
    Word           Root        Suffix    Level       Normalized  
govern         govern      -         Base        govern      
government     govern      ment      Level-1     govern      
governance     govern      ance      Level-1     govern      

