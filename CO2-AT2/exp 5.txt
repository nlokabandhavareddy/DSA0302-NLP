words = ["create", "creates", "creating"]

for word in words:

    root = "create"

    if word == "create":
        suffix = "-"
        grammar = "Base Form"

    elif word.endswith("s"):
        suffix = "s"
        grammar = "Third Person Singular"

    elif word.endswith("ing"):
        suffix = "ing"
        grammar = "Present Participle"

    print("Original :", word)
    print("Suffix :", suffix)
    print("Grammar :", grammar)
    print("Root :", root)
    print("Normalized :", root)
    print("-----------------------")
#OUTPUT
    Original : create
Suffix : -
Grammar : Base Form
Root : create
Normalized : create
-----------------------
Original : creates
Suffix : s
Grammar : Third Person Singular
Root : create
Normalized : create
-----------------------
Original : creating
Suffix : ing
Grammar : Present Participle
Root : create
Normalized : create
