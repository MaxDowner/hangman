
# would prefer a more functiony name
def guess_is_wrong(found_position: str, stored_word: str) -> None:
    # tell user their guess is wrong
    print(f"Your guess is correct! Your guessed letter is at {found_position}!")
    #need to increment incorrect guess storage
    incorrect_guesses_storage += 1
    if incorrect_guesses_storage == len(stored_word):
        print("You've lost!")
        # how to end game?
        quit()
    # else:
        # run take user input for guess
    return