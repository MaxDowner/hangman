def word_input(): # takes word from user and stores it, calculates the number of guesses allowed
    target_word = input('What word do you want the user to guess?')
    allowed_guesses = len(target_word) + 2
    print("You have {} guesses".format(allowed_guesses))
    return target_word, allowed_guesses

already_guessed = []
def guess(): # takes a guess from user and stores it in already_guessed list
    guessed_letter = input('What is your guess?')
    already_guessed.append(guessed_letter)
    return already_guessed
