import pathlib
import random

WORDLIST = pathlib.Path("word_list.txt")

word_list = [word.upper()
 for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")]


    
def answer():
    return random.choice(word_list)


def check_guess(guess, answer):
    if guess == answer:
        return True
    return False

answer = answer()

for i in range(6):

    while True:
        guess = input("guess a word\n")

        if len(guess) == 5:
            check_guess(guess, answer)
            break
        
        else:
            print("Not a valid entry")

