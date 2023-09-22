import string
import math

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Presidents                 |
# Alexander Ellingsen                   |
# Last Modified: November 9, 2022       |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class President:
# Sets up president calss with first, last, number of pres, date they started, term length, and occupation before
    def __init__(self, first, last, number, start_in, term, occupation):
        self.name = first + " " + last
        self.number = number
        self.occupation = occupation
        self.time_in_office = term
        self.start_in = start_in
# Getter functions
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def get_occupation(self):
        return self.occupation
    def get_time_in_office(self):
        return self.time_in_office
# Sets up print_all_presidents function
    def __str__(self):
        return "No. " + str(self.number) + " " + "(" + str(self.start_in) + ") " + str(self.name)


def print_by_name(listing, n):
    print("")
# Determines if string is above 3 characters
    if len(str(n)) < 3:
        print("Please try 3 or more characters.")
    else:
# Adds names to a list that contain the input
        printed_names = []
        for i in listing:
            big_name = str(i.get_name())
            input_name = str(n)
            if input_name.upper() in big_name.upper():
                printed_names.append(str(i))
#CHecks if there are names that include the input
        if len(printed_names) > 0:
            for i in printed_names:
                print(str(i))
        else:
            print("No president's name contains '" + n + "'")

def print_by_number(listing, n):
# Takes input and converts it to work for index
    real_num = int(n) - 1
# CHecks if the number is valid
    if n <= 46 and n >= 1:
        place = (listing[real_num])
        print("\n" + str(place))
    else:
        print("\nPresident number must be between 1 and 46")

def count_by_occupation(listing, o):
    printeds_occupation = []
    printed_occupation = []
    string = " "
    count = 0
# Adds occupations to a list
    for i in listing:
        big_occupation = i.get_occupation()
        if o in big_occupation:
            printeds_occupation.append(i.get_name())
# Grover Cleveland clause
    for i in printeds_occupation:
        if i not in printed_occupation:
            printed_occupation.append(i)
            count += 1
    print("\n" + str(count) + " " + o + " " + "presidents: " + string.join(printed_occupation))

def average_term_length(listing):
    total = 0.0
#Adds all term lengths together
    for i in listing:
        total_term = float(str(i.get_time_in_office()))
        num_term = int(total_term)
        total += num_term
#Rounds to the nearest number
    int_total = math.ceil(total/46)
    print("\nAverage term length, about " + str(int_total) + " years")
        


 
# ---------------------------------------

def print_menu():
    print ("""
1. Print all presidents
2. Print president by name
3. Print president by number
4. Count presidents with occupation
5. Print average term length
6. Quit
    """)
# ---------------------------------------

def print_all_presidents(pres_listing):
    for president in pres_listing:
        print(president)
    
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pres_listing(filename):
    pres_listing = []
    file = open(filename, "r")
    
    for president in file:
        presilist = president.strip().split(",")
        number = int(presilist[0])               # number
        last = presilist[1]                      # last name
        first = presilist[2]                     # first name
        start_in = int(presilist[3])             # first year in office
        term = float(presilist[4])               # years in office
        occupations = []
        for position in range(5, len(presilist)):
            occupations += [presilist[position]] # occupation
        pres_listing += [President(first, last, number, start_in, term, occupations)]

    file.close()
    return pres_listing

# ---------------------------------------

def get_choice(low, high, message):
    
    legal_choice = False
    answer = input(message)
    while answer == "":
        answer = input(message)
    for char in answer:
        if char not in string.digits:
            print('ERROR: ', answer, "is not a number")
            return 0
    answer = int(answer)
    if (low > answer) or (answer > high):
        print('ERROR: ', answer, "is not a choice")
        return 0

    return answer

# ---------------------------------------

def main():
    pres_listing = create_pres_listing("pres_listing.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_all_presidents(pres_listing)
        elif choice == 2:
            name = input("Enter a president name: ").lower()
            print_by_name(pres_listing, name)
        elif choice == 3:
            number = get_choice(1, 46, "Enter a president number: ")
            print_by_number(pres_listing, number)
        elif choice == 4:
            occupation = input("Enter a president occupation: ").lower()
            count_by_occupation(pres_listing, occupation)
        elif choice == 5:
            average_term_length(pres_listing)
        elif choice == 6:
            print("Thank you.  Goodbye!")

# ---------------------------------------

main()
