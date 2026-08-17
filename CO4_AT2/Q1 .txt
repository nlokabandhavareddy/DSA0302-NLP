Program
# Banking Customer Support Chatbot
# CFG and ambiguity analysis


sentence = "Show me the transactions with the card from last month"


print("===== BANKING CHATBOT =====")
print("Input:", sentence)
print()


print("Possible Interpretation 1:")
print("Transactions made using the card")
print("Time: Last Month")
print()


print("Possible Interpretation 2:")
print("Transactions associated with a card")
print("Card reference: Last Month")
print()


print("CFG Analysis:")
print("The sentence contains an ambiguous prepositional phrase.")
print("'with the card' can have multiple attachments.")
print()


print("Improved Parsing:")
print("Parser      : Earley Parser")
print("Disambiguation: PCFG")
print("Agreement   : Feature Structures")
print()


print("Final Interpretation:")
print("Action      : Show")
print("Object      : Transactions")
print("Card        : Used for transactions")
print("Time        : Last Month")
Output
===== BANKING CHATBOT =====
Input: Show me the transactions with the card from last month


Possible Interpretation 1:
Transactions made using the card
Time: Last Month


Possible Interpretation 2:
Transactions associated with a card
Card reference: Last Month


CFG Analysis:
The sentence contains an ambiguous prepositional phrase.
'with the card' can have multiple attachments.


Improved Parsing:
Parser      : Earley Parser
Disambiguation: PCFG
Agreement   : Feature Structures


Final Interpretation:
Action      : Show
Object      : Transactions
Card        : Used for transactions
Time        : Last Month
