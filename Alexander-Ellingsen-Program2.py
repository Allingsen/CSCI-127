# -----------------------------------------+
# Alexander Ellingsen                      |
# CSCI 127, Program 2                      |
# Last Updated: (10/05/2022)               |
# Name:                                    |
# -----------------------------------------|
# Poker Hand Evaluation                    |
# -----------------------------------------+


# Helper Function
# Given a poker hand as a list, return a list of the ranks
def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result
 

def five_of_a_kind(hand):
    # Makes sure the first card is always a joker then the rest have the same number
    if hand[0][1] == "?" and hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    else:
        return False 
    
def straight_flush(hand):
    # Checks if the cards have descending value (from the last one) and have the same suit
    if hand[4][0] == hand[3][0]+1 == hand[2][0]+2 == hand[1][0]+3 == hand[0][0]+4 and hand[4][1] == hand[3][1] == hand[2][1] == hand[1][1] == hand[0][1]:
        return True
    else:
        return False

def straight(hand):
    # Checks if the cards have descending value (from the last one)
    if hand[4][0] == hand[3][0]+1 == hand[2][0]+2 == hand[1][0]+3 == hand[0][0]+4:
        return True
    else:
        return False

def four_of_a_kind(hand):
    # Checks if the first four cards have the same value or the last four cards have the same value
    if hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0] or hand[1][0] ==hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    else:
        return False

def full_house(hand):
    # Checks if the first three cards have the same value and the last two cards have the same value
    if hand[0][0] == hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return True
    # Checks if the first two cards have the same value and the last three cards have the same value
    elif hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    else:
        return False

def flush(hand):
    # Checks if all the cards have the same suit
    if hand[4][1] == hand[3][1] == hand[2][1] == hand[1][1] == hand[0][1]:
        return True
    else:
        return False

def three_of_a_kind(hand):
    # Checks if the first three, middle three, or last three cards have the same value
    if hand[0][0] == hand[1][0] == hand[2][0] or hand[1][0] == hand[2][0] == hand[3][0] or hand[2][0] == hand[3][0] == hand[4][0]:
        return True
    else:
        return False

def two_pair(hand):
    # Checks if the first two cards have the same value and the middle two cards have the same value
    if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
        return True
    # Checks if the first two cards have the same value and the last two cards have the same value
    elif hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
        return True
    # Checks if the middle two cards have the same value and the last two cards have the same value
    elif hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
        return True
    else:
        return False

def pair(hand):
    # Checks if the first two cards, second two cards, middle two cards, or last two cards have the same value
    if hand[0][1] == hand[1][1] or hand[1][1] == hand[2][1] or hand[2][1] == hand[3][1] or hand[3][1] == hand[4][1]:
        return True
    else:
        return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    # Notice that once a hand is identified, no further evaluations are tried
    # Ex. A four of a kind is also a three of a kind, but evalutes to four of a kind
    poker_hand.sort() 
    print(poker_hand, "Poker Hand: ", end="")
    if five_of_a_kind(poker_hand):
        print("Five of a Kind")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand):
        print("Four of a Kind")
    elif full_house(poker_hand):
        print("Full House")
    elif flush(poker_hand):
        print("Flush")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand):
        print("Three of a Kind")
    elif two_pair(poker_hand):
        print("Two Pair")
    elif pair(poker_hand):
        print("One Pair")
    else:
        print("Nothing") # Can only beat another hand with nothing. (High card wins)
		
# -----------------------------------------+

def main():
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14 # Ace always ranks highest
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    # The inline comments show how the card should be evaluted by the functions you write
    # The hands below are shown in order from worst to best. (ie: flush beats straight) 
    evaluate([[2, "♠"], [7, "♣"], [8, "♦"], [A, "♦"], [Q, "♥"]])    # High card
    evaluate([[T, "♠"], [Q, "♣"], [6, "♦"], [9, "♦"], [Q, "♥"]])    # One pair
    evaluate([[T, "♠"], [9, "♣"], [6, "♦"], [9, "♦"], [6, "♥"]])    # Two pair
    evaluate([[K, "♦"], [7, "♣"], [7, "♥"], [8, "♣"], [7, "♠"]])    # Three of a kind
    evaluate([[T, "♣"], [9, "♣"], [6, "♣"], [7, "♣"], [8, "♠"]])    # Straight
    evaluate([[2, "♥"], [9, "♥"], [3, "♥"], [6, "♥"], [T, "♥"]])    # Flush
    evaluate([[8, "♦"], [7, "♣"], [8, "♥"], [8, "♣"], [7, "♠"]])    # Full house
    evaluate([[2, "♦"], [7, "♣"], [2, "♥"], [2, "♣"], [2, "♠"]])    # Four of a kind
    evaluate([[T, "♣"], [9, "♣"], [6, "♣"], [7, "♣"], [8, "♣"]])    # Straight flush    
    evaluate([[7, "♥"], [0, "?"], [7, "♦"], [7, "♣"], [7, "♠"]])    # 5 of a kind ([0, "?"] is the Joker)

    
    print("---------------------------------------")   
    print("Honor's Section Challenge:")
    evaluate([[3, "♣"], [4, "♣"], [2, "♣"], [A, "♣"], [5, "♠"]])    # stright (with low ace)
    evaluate([[3, "♥"], [0, "?"], [4, "♣"], [6, "♥"], [7, "♦"]])    # stright (with joker)

# -----------------------------------------+

main()
