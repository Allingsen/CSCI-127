# -----------------------------------------+
# Alex Ellingsen                           |
# CSCI 127, Lab 3                          |
# Last Updated: (09/13/2022)               |
# Name:                                    |
# -----------------------------------------|
# Random letter from string                |
# -----------------------------------------+


import string
import random



current_string = ""

def print_random_letter(string):
    
    #Determinesif the digit is a letter
    randlet = random.choice(current_string)
    randind = str(current_string.index(randlet))
    char = randlet in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    #Determines if there are any letters in the string
    nospace = current_string.replace(" ", "")
    lett = nospace.upper()
    letters = lett.isupper()

    if letters is True: #If letters are present, return true
        
        if char is True: #If digit is a letter, return true
            print("Randomly chose the " + randlet + " at index " + randind)
        else:
            print_random_letter(current_string)
            
    else:
        print("Error:The current string has no letters in it.")
        
def main(): 
    menu = '''
Thank you for running Lab Assignment 3
Please read carefully as our menu options may have changed:

Please press:
'E' - to enter a different string of text
'R' - to randomly choose a letter from the text
'M' - to repeat this menu again
'Q' - to quit this program

Current string:
012345....10...15...20...25...30...
↓↓↓↓↓↓↓↓↓↓↓    ↓    ↓    ↓    ↓'''
    global current_string
    current_string = "The quick red fox jumps over the lazy brown dog."
    
    print(menu)
    print(current_string)
    print()
    over = False
    while(not over):
        x = input("Enter your choice: ").upper()
        while (x != 'E') and (x != 'R') and (x != 'M') and (x != 'Q'):
            x = input("You must enter E, C, R, or Q: ").upper()
        if x == 'E':
            current_string = input("Enter the new string: ")
            print("Current string set to: ", current_string)
        elif x == 'R':
            print_random_letter(current_string)
        elif x == 'M':
            print(menu)
            print(current_string)
            print()
        else:
            over = True
            print("Goodbye.")
                 
main()
