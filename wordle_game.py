
end_of_game = False

while not end_of_game:

    while True:
        guess = input("guess a word\n")

        if len(guess) == 5:
            break
        else:
            print("Not a valid entry")

    
