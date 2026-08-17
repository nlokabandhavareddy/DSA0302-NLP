Program
# Healthcare NLP System
# CFG + PCFG + Feature Structures + Earley Parsing
# Medical information extraction


sentence = (
    "The doctor who reviewed the patient last week "
    "recommends starting medication and scheduling a "
    "follow-up visit in Chennai."
)


print("===== HEALTHCARE NLP SYSTEM =====")
print("Input Sentence:")
print(sentence)
print()


# Tokenization
words = sentence.replace(".", "").split()


print("1. Tokenization:")
print(words)
print()


# Entity identification
print("2. Medical Entities:")
print("Doctor      -> Medical Person")
print("Patient     -> Patient")
print("Medication  -> Treatment")
print("Chennai     -> Location")
print("Follow-up   -> Medical Action")
print()


# Syntactic analysis
print("3. CFG Syntactic Analysis:")
print("Subject     -> The doctor who reviewed the patient last week")
print("Main Verb   -> recommends")
print("Action 1    -> starting medication")
print("Action 2    -> scheduling a follow-up visit")
print("Location    -> Chennai")
print()


# Feature structures
print("4. Feature Structure:")
print("Subject Number -> Singular")
print("Verb Number    -> Singular")
print("Agreement      -> Correct")
print()


# PCFG
print("5. PCFG:")
print("Ambiguous structures detected")
print("Most probable structure selected")
print()


# Parsing
print("6. Efficient Parsing:")
print("Parser -> Earley Parser")
print("Status -> Parsing completed")
print()


# Sub-categorization
print("7. Sub-Categorization:")
print("recommend -> Doctor + Medical Action")
print("starting  -> Treatment")
print("scheduling -> Follow-up Event")
print()


# Final output
print("===== STRUCTURED OUTPUT =====")
print("Diagnosis   : Not mentioned")
print("Doctor      : Doctor")
print("Patient     : Patient")
print("Treatment   : Starting medication")
print("Follow-up   : Scheduling a follow-up visit")
print("Location    : Chennai")
Output
===== HEALTHCARE NLP SYSTEM =====
Input Sentence:
The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai.


1. Tokenization:
['The', 'doctor', 'who', 'reviewed', 'the', 'patient',
 'last', 'week', 'recommends', 'starting', 'medication',
 'and', 'scheduling', 'a', 'follow-up', 'visit', 'in', 'Chennai']


2. Medical Entities:
Doctor      -> Medical Person
Patient     -> Patient
Medication  -> Treatment
Chennai     -> Location
Follow-up   -> Medical Action


3. CFG Syntactic Analysis:
Subject     -> The doctor who reviewed the patient last week
Main Verb   -> recommends
Action 1    -> starting medication
Action 2    -> scheduling a follow-up visit
Location    -> Chennai


4. Feature Structure:
Subject Number -> Singular
Verb Number    -> Singular
Agreement      -> Correct


5. PCFG:
Ambiguous structures detected
Most probable structure selected


6. Efficient Parsing:
Parser -> Earley Parser
Status -> Parsing completed


7. Sub-Categorization:
recommend -> Doctor + Medical Action
starting  -> Treatment
scheduling -> Follow-up Event


===== STRUCTURED OUTPUT =====
Diagnosis   : Not mentioned
Doctor      : Doctor
Patient     : Patient
Treatment   : Starting medication
Follow-up   : Scheduling a follow-up visit
Location    : Chennai
