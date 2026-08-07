# Morphological Parsing

words = ["activate", "activation", "reactivation"]

print("{:<15}{:<10}{:<12}{:<10}{:<25}".format(
    "Word", "Prefix", "Root", "Suffix", "Sequence"))

for word in words:

    prefix = "-"
    suffix = "-"

    if word == "activate":
        root = "activate"
        sequence = "Base"

    elif word == "activation":
        root = "activate"
        suffix = "ion"
        sequence = "activate -> activation"

    elif word == "reactivation":
        prefix = "re"
        root = "activate"
        suffix = "ion"
        sequence = "re + activate + ion"

    print("{:<15}{:<10}{:<12}{:<10}{:<25}".format(
        word, prefix, root, suffix, sequence))
#OUTPUT
    Word           Prefix    Root        Suffix    Sequence                 
activate       -         activate    -         Base                     
activation     -         activate    ion       activate -> activation   
reactivation   re        activate    ion       re + activate + ion
