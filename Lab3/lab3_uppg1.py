
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

def wordlist1():
    list_of_words = list()
    list_of_definitions = list()

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
        program_state = int(input("Choose alternative: "))
            # Insert
        if program_state == 1:
            print("Insert word and definition")
            word = input("Word: ")
            definition = input("Definition: ")
            list_of_words.append(word)
            list_of_definitions.append(definition)

            # Lookup
        elif program_state == 2:
            print("Lookup definition for word")
            word = input("Word: ")

            # Check if word is in list
            # If yes, get index
            # print both lists at index
            n = 0
            # flagga för att hålla koll på om ordet hittats.
            found = False
            while n < len(list_of_words):
                if word == list_of_words[n]:
                    print("index of", word, "is:", int(n))
                    print("Definition:", list_of_definitions[int(n)])
                    found = True

                    # alernativt n = len(list_of_words)
                    break
                else:
                    n += 1
            if found == False:
                print("ERROR! Word", word, "is not in the list, yeeting you back to menu.")


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
# Theo tupp, dsvdv

def wordlist2():

    cool_list = list()
    word_and_def = tuple()

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
        program_state = int(input("Choose alternative: "))

        found = False

        # Insert
        if program_state == 1:
            print("Insert word and definition")
            word = str(input("Word: "))
            definition = str(input("Definition: "))
            
            word_and_def = (word, definition)
            cool_list.append(word_and_def)

        # Lookup
        elif program_state == 2:
            print("Lookup definition for word")
            word = input("Word: ")

            n = 0
            while n < len(cool_list):
                if word == cool_list[n][0]:
                    found = True
                    print("Definition:", cool_list[n][1])
                n += 1
            if found == False:
                print("ERROR! Not a valid input. Word is not in the list")
            found = False


        # Exit
        elif program_state == 3:
            print("Exiting program")
            return 

        # Delete. Inte jättesnyggt men det funkar.
        elif program_state == 4:
            print("Delete item")
            word = input("Word: ")

            n = 0
            while n < len(cool_list):
                if word == cool_list[n][0]:
                    definition = cool_list[n][1]
                    cool_list.remove((word, definition))
                    print(cool_list)
                    found = True
                n += 1
            if found == False:
                print("ERROR! Word is not in the list")    

        # Misinput check
        else:
            print("Not a valid input")



#wordlist2()
# ------------------------------------------------------------------
# Uppgift 3
# Ett dictionary

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
        program_state = int(input("Choose alternative: "))

        # Found flagga
        found = False

        # Insert
        if program_state == 1:
            print("Insert word and definition")
            word = str(input("Word: "))
            definition = str(input("Definition: "))

            worddef_dict[word] = definition

        elif program_state == 2:
            print("Lookup definition for word")
            word = input("Word: ")
            if word in worddef_dict:
                found = True
                print("Definition:", worddef_dict.get(word))

            if found == False:
                print("ERROR! Not a valid input. Word is not in the list")
            found = False

        # Exit
        elif program_state == 3:
            print("Exiting program")
            return 

        elif program_state == 4:
            print("Delete dict entry")
            word = input("Word: ")
            if word in worddef_dict:
                found == True
                worddef_dict.pop(word)
                print(worddef_dict)
            elif found == False:
                print("ERROR! Word not in list.")

        # Misinput check
        else:
            print("Not a valid input")


wordlist3()