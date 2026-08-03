import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

while True:
    print("\nMenu")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
        print("Dates:", result)

    elif choice == 2:
        result = re.findall(r'\b[6-9]\d{9}\b', text)
        print("Phone Numbers:", result)

    elif choice == 3:
        result = re.findall(r'#\w+', text)
        print("Hashtags:", result)

    elif choice == 4:
        result = re.findall(r'@\w+', text)
        print("Mentions:", result)

    elif choice == 5:
        prefix = input("Enter Prefix: ")
        result = re.findall(r'\b' + prefix + r'\w*', text)
        print(result)

    elif choice == 6:
        suffix = input("Enter Suffix: ")
        result = re.findall(r'\b\w*' + suffix + r'\b', text)
        print(result)

    elif choice == 7:
        word = input("Enter Word: ")
        result = re.findall(r'\b' + word + r'\b', text)
        print(result)

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")