Program
# Voice Assistant Flight Booking
# Top-Down Parsing vs Earley Parsing


command = "Book a flight to Delhi with a window seat"


print("===== VOICE ASSISTANT =====")
print("Command:", command)
print()


print("Possible Parse Structures:")
print()


print("Parse 1:")
print("Action      : Book")
print("Object      : Flight")
print("Destination : Delhi")
print("Seat        : Window Seat")
print()


print("Parse 2:")
print("Action      : Book")
print("Flight      : To Delhi")
print("Preference  : Window Seat")
print()


print("Top-Down Parsing:")
print("Problem     : Backtracking")
print("Problem     : Multiple parse attempts")
print("Problem     : Difficult with incomplete input")
print("Problem     : Real-time delay")
print()


print("Earley Parsing:")
print("Handles ambiguity       : Yes")
print("Handles partial input   : Yes")
print("Reduces repeated work   : Yes")
print("Suitable for real-time  : Yes")
print()


print("Final Interpretation:")
print("Action      : Book Flight")
print("Destination : Delhi")
print("Seat        : Window Seat")
Output
===== VOICE ASSISTANT =====
Command: Book a flight to Delhi with a window seat


Possible Parse Structures:


Parse 1:
Action      : Book
Object      : Flight
Destination : Delhi
Seat        : Window Seat


Parse 2:
Action      : Book
Flight      : To Delhi
Preference  : Window Seat


Top-Down Parsing:
Problem     : Backtracking
Problem     : Multiple parse attempts
Problem     : Difficult with incomplete input
Problem     : Real-time delay


Earley Parsing:
Handles ambiguity       : Yes
Handles partial input   : Yes
Reduces repeated work   : Yes
Suitable for real-time  : Yes


Final Interpretation:
Action      : Book Flight
Destination : Delhi
Seat        : Window Seat
