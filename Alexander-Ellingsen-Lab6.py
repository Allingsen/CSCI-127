# -----------------------------------------+
# Your name                                | 
# CSCI 127, Lab 6                          |
# Last Updated: (mm/dd/yyyy)               |
# Name:                                    |
# -----------------------------------------|
# Get states in a population range         |
# -----------------------------------------+


def get_list_from_file(census_data):
    
    census_file = open("census2020.txt", "r")
    states = []
    
    for one_line in census_file:
        values = one_line.split()
        states.append(values)
      
    return states

def get_listing_in_range(lower, upper, state_list):
    
    lists = []
    listing = ''
    count = 0
    namez = []
    pops = []
    
    for i in state_list:
        millions = round((((int(state_list[state_list.index(i)][1])) / 1000000)), 2)
        if millions > lower and millions < upper:
            count = count + 1
            lists.append(state_list[state_list.index(i)])
            
    rist = lists[::-1]
    
    for e in rist:
        namez.append(rist[rist.index(e)][0])
        pops.append(str(round((((int(rist[rist.index(e)][1])) / 1000000)), 2)))
        listing = '\t' + '\n\t'.join(namez) + '\t' + ' '.join(pops) + '\n'
    # I couldnt figure out the formatting         


    print(count, "States have a population between", lower, "and", upper, "million:")
    return listing
    
def main():
    # TODO: complete the get_list_from_file() function
    states = get_list_from_file("census2020.txt")
    print("\n ***first state in list:", states[0][0], '*** \n') # should be California
    
    print("The least populous U.S. state: Wyoming with just over 0.5 million")
    print("The most populous U.S. state: California with almost 40 million")
    print("Enter two numbers between 0.5 and 40 to list states in that range.")
    lo = float(input("Enter lower bound: "))
    hi = float(input("Enter upper bound: "))
    
    # TODO: complete the function called get_listing_in_range(); make it a pure function
    # The return value should be a string.
    # Each state and population in that range should appear on its own line,
    # ordered by population from lowest to highest.
    
    listing = get_listing_in_range(lo, hi, states)
    print(listing)
    print("\n ***first state in list:", states[0][0], '*** \n') # should be California

main()
