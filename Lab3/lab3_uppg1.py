
#Uppgift 1.
# 3 st ordlistor:
'''
1- Två stycken listor av strängar. Den första listan innehåller ordet vi vill slå upp, och den andra listan innehåller beskrivningen för det ordet, på motsvarande position.
2- En lista av tupler. En enda lista som består av par, där första delen av varje par är ordet vi vill slå upp, och den andra är beskrivningen. Observera här alltså att datastrukturen ska vara en lista, varje element i denna lista ska i sin tur vara ett par (en tupel med två element).
3- Ett dictionary. Ett dictionary som innehåller ordet vi vill slå upp som "nyckel" och tillhörande beskrivning som "värde".
'''
# -------------------------------------------------------------------
# Ordlista 1,
# med 2 listor av strängar

def list_insert(words, definitions):
    # Insert
    word = input("Word: ")
    if word not in words:
        definition = input("Definition: ")

        words.append(word)
        definitions.append(definition)
    else:
        print(word, "already in list")



def list_lookup(words, definitions):
    word = input("Word: ")

    # Check if word is in list
    # If yes, get index
    if word in words:
        word_i = words.index(word)
        print("index of", word, "is:", word_i)
        print("Definition:", definitions[word_i])
    else:
        print("ERROR! Word", word, "is not in the list, yeeting you back to menu.")




def wordlist1():
    words = list()
    definitions = list()

    # Loopen som får programmet att köras kontinuerligt,
    # tills nedstängning önskas
    while True:
            # State machine elr nåt
        # "Menyn"
        print(
        "---------------------\n",
        "Menu overview:\n",
        "1: Insert\n",
        "2: Lookup\n",
        "3: Exit program"
        )
        
        try:
            program_state = int(input("Choose alternative: "))
            print("You chose:", program_state)
        except ValueError:
            print("Not an int.")
            continue

            # Insert
        if program_state == 1:
            print("Insert word and definition")
            list_insert(words, definitions)

            # Lookup
        elif program_state == 2:
            print("Lookup definition for word")
            list_lookup(words, definitions)

            # Exit
        elif program_state == 3:
            print("Exiting program")
            return 

        # Misinput check
        else:
            print("Not a valid input")


#wordlist1()

# ------------------------------------------------------------------
# Uppgift 2
# En lista med tuplar
def tuple_insert(tuples_list, word_and_def):

    word = str(input("Word: "))
    if word not in tuples_list:
        definition = str(input("Definition: ")) 
        word_and_def = (word, definition)
        tuples_list.append(word_and_def)
    else:
        print(word, "not in list.")

def tuple_lookup(tuples_list):
    word = input("Word: ")
    found = False
    for word_i, definition in tuples_list:
        if word_i == word:
            print("Definition:", definition)
            found = True
    if not found:
        print("WORD NOT IN LIST!")

def word_delete(tuples_list):
    word = input("Word: ")
    found = False
    n = 0
    while n < len(tuples_list):
        if word == tuples_list[n][0]:
            definition = tuples_list[n][1]
            tuples_list.remove((word, definition))
            print("The updated list is now:", tuples_list)
            found = True
        n += 1
    if not found:
        print("WORD NOT IN LIST!")    

def wordlist2():

    tuples_list = list()
    word_and_def = tuple()

    while True:
        # State machine typ
        # "Menyn"
        print(
        "---------------------\n",
        "Menu overview:\n",
        "1: Insert\n",
        "2: Lookup\n",
        "3: Exit program\n",
        "4: (Delete item)"
        )
        try:
            program_state = int(input("Choose alternative: "))
            print("You chose:", program_state)
        except ValueError:
            print("Not an int.")
            continue

        # Insert
        if program_state == 1:
            print("Insert word and definition")
            tuple_insert(tuples_list, word_and_def)

        # Lookup
        elif program_state == 2:
            print("Lookup definition for word")
            tuple_lookup(tuples_list)

        # Exit
        elif program_state == 3:
            print("Exiting program")
            return 

        # Delete. Inte jättesnyggt men det funkar.
        elif program_state == 4:
            print("Delete item")
            word_delete(tuples_list)
            word = input("Word: ") 

        # Misinput check
        else:
            print("Not a valid input")


#wordlist2()

# ------------------------------------------------------------------
# Uppgift 3
# Ett dictionary

def dict_input(worddef_dict):
    word = str(input("Word: "))
    definition = str(input("Definition: "))

    worddef_dict[word] = definition

def dict_lookup(worddef_dict):
    word = input("Word: ")
    if word in worddef_dict:
        print("Definition:", worddef_dict.get(word))
    
    else:
        print("ERROR! Not a valid input. Word is not in the dict")

def dict_delete(worddef_dict):
    word = input("Word: ")
    if word in worddef_dict:
        worddef_dict.pop(word)
        print(worddef_dict)
    else:
        print("ERROR! Word not in list.")


def wordlist3():
    worddef_dict = dict()
    
    while True:
        # State machine elr nåt
        # "Menyn"
        print(
        "---------------------\n",
        "Menu overview:\n",
        "1: Insert\n",
        "2: Lookup\n",
        "3: Exit program\n",
        "4: (Delete item)"
        )
        try:
            program_state = int(input("Choose alternative: "))
            print("You chose:", program_state)
        except ValueError:
            print("Not an int.")
            continue

        # Found flagga
        found = False

        # Insert
        if program_state == 1:
            print("Insert word and definition")
            dict_input(worddef_dict)

        elif program_state == 2:
            print("Lookup definition for word")
            dict_lookup(worddef_dict)

        # Exit
        elif program_state == 3:
            print("Exiting program")
            return 

        elif program_state == 4:
            print("Delete dict entry")
            dict_delete(worddef_dict)

        # Misinput check
        else:
            print("Not a valid input")


wordlist3()