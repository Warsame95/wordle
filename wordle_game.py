import pathlib

WORDLIST = pathlib.Path("word_list.txt")

word_list = [word.upper()
 for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")]

print(word_list[1])


for i in range(6):

    while True:
        guess = input("guess a word\n")

        if len(guess) == 5:
            break
        else:
            print("Not a valid entry")



    
