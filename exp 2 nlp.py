# Finite State Automaton (FSA)
# Recognizes strings ending with "ab"

def fsa_ends_with_ab(string):
    state = "q0"

    for ch in string:
        if state == "q0":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == "b":
                state = "q2"
            elif ch == "a":
                state = "q1"
            else:
                state = "q0"

        elif state == "q2":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"

    if state == "q2":
        return True
    else:
        return False


# Main Program
text = input("Enter a string: ")

if fsa_ends_with_ab(text):
    print("Accepted: String ends with 'ab'")
else:
    print("Rejected: String does not end with 'ab'")
