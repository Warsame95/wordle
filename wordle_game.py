import pathlib
import random

WORDLIST = pathlib.Path("word_list.txt")

word_list = [word.upper()
 for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")]


def create_board():
    global board
    _ = "_"
    board = [[_,_,_,_,_],
             [_,_,_,_,_],
             [_,_,_,_,_],
             [_,_,_,_,_],
             [_,_,_,_,_],
             [_,_,_,_,_]]

def print_board():
    for i in range(6):
        for j in range(5):
            print(board[i][j]+ " ", end="")
        print()     

    
def answer():
    return random.choice(word_list)


def check_guess(guess, answer):
    if guess == answer:
        return True
    return False

def main():

    answer = answer()

    for i in range(6):

        while True:
            guess = input("guess a word\n")

            if len(guess) == 5:
                check_guess(guess, answer)
                break
        
            else:
                print("Not a valid entry")

create_board()
print_board()
