import pathlib
import random
from rich import print
from rich.console import Console
from rich.theme import Theme
import sys
from termcolor import colored

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
    if guess.upper() == answer.upper():
        return True
    return False

""" def add_colour(guess, answer):
    for letter, correct in zip(guess, answer):
        if letter == correct: """

def success_message():
    print("Cogratulations, you got the word correct!!")

def fail_message(answer):
    print("The word is " + answer)

def add_guess(guess, answer):
    for i in range(6):
        if board[i][0] == "_":
            for j in range(5):
                #print(guess.upper()[j] + " " + answer[j])
                if guess.upper()[j] == answer[j]:
                    style = "bold white on green"
                elif guess.upper()[j] in answer:
                    style = "bold white on yellow"
                else:
                    style = "white on #666666"
                
                board[i][j] = f"[{style}]{guess.upper()[j]}"
            break

answer = answer()

def main():


    for i in range(6):

        while True:
            guess = input("guess a word\n")

            if len(guess) == 5:
                add_guess(guess, answer)
                print_board()
                break
        
            else:
                print("Not a valid entry")
        
        if check_guess(guess, answer):
            return success_message()
        
        elif i == 5:
            return fail_message(answer)

create_board()
main()
