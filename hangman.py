def play(word):
    def split(word):
        return [char for char in word]

    comp_word = split(word)
    used_letters = []
    counter = 0
    print('The word is', len(word), 'letters long.')

    while counter < 6:
        user_guess = input("Please guess a letter: ")
        user_guess = user_guess.lower()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in used_letters:
                print("You already tried", user_guess, ".")
            elif user_guess not in word:
                print('The letter', user_guess, 'is not in the word.')
                counter += 1
                used_letters.append(user_guess)
            else:
                print('The letter', user_guess, 'is in the word.')
                used_letters.append(user_guess)







word = "Champions".lower()
play(word)
