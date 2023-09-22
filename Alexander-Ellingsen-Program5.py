import random

# -------------------------------------------------
# CSCI 127, Program 5: WORDLE
# November 29, 2022
# Alexander Ellingsen
# -------------------------------------------------

class Wordle:

    def __init__(self, letters_in_word, file_of_words):
        self.num_letters = letters_in_word
        self.word_list = open(file_of_words, 'r').read().upper().splitlines()
        self.answer = self.word_list[random.randint(0, len(self.word_list)-1)]
        self.cheat_code = "?"
        self.test_code = "!"
        self.turn_num = 0

    def change_answer(self, new_answer):
        self.answer = new_answer.upper()

    def get_player_guess(self):
        self.turn_num += 1
        user_word = input("Enter your guess: ").upper()
        word_list = open('knuth5letterwords.csv', 'r').read().upper().splitlines()
        if(user_word == self.cheat_code):
            self.turn_num -= 1
            print("\tPsst. Answer is", self.answer)
            user_word = self.get_player_guess()
        if(user_word == self.test_code):
            self.turn_num -= 1
            new_answer = input("\tOkay. Enter the new answer: ").upper()
            while new_answer not in self.word_list:
                new_answer = input("\tEnter a valid " + str(self.num_letters) + " letter word: ").upper()
            self.change_answer(new_answer)
            print("\tAnswer set to " + new_answer.upper())
            user_word = self.get_player_guess()
        if len(user_word) != 5:
            self.turn_num -= 1
            print("\tYour word must have 5 letters.")
            user_word = self.get_player_guess()
        if user_word not in word_list:
            self.turn_num -= 1
            print("\t" + user_word + " isn't in the list of valid words.")
            user_word = self.get_player_guess()
        
        return (user_word.upper())

    def generate_hint(self, guess):
        print('\n\t' + guess)
        hint = ""
        hint_list = []
        if(guess == self.answer):
            return guess # Game over!

        if guess != self.answer:
            for g in guess:
                if g not in self.answer:
                    hint_list.append('-')
                else:
                    for i in self.answer:
                        if i == g and guess.index(i) == self.answer.index(i):
                            if g.lower() not in hint_list:
                                hint_list.append(g)
                        elif g == i:
                            if g.lower() not in hint_list:
                                hint_list.append(g.lower())
                    
        hint = hint.join(hint_list)           
        return(hint)

def main(file):

    game = Wordle(5, file)
    print("\nWelcome to WORDLE!\n")
    guess = ""
    
    
    while(guess != game.answer and game.turn_num < 6):
        print(game.turn_num+1, end='. ')
        guess = game.get_player_guess()
        print('\t'+ game.generate_hint(guess) + '\n')
    if guess == game.answer:
        if guess == game.answer and game.turn_num == 1:
            print("Wow! You're wither very lucky, or you got some insider information.")
        elif guess == game.answer and game.turn_num == 6:
            print("Phew! You got it on the last try!")
        else:
            print("Great! You got it in " + str(game.turn_num) + " tries.")
    if game.turn_num == 6:
        reveal = input("Game Over. Reaveal answer> y/n: ").lower()
        if reveal == "y":
            print("Answer was " + game.answer)
        else:
            print("Thanks for playing.\n")
    
if __name__ == "__main__":
    main("knuth5letterwords.csv")
