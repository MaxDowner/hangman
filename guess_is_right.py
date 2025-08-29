

# would prefer a more functiony name
def guess_is_right(found_position: str, stored_word: str) -> None:
    # tell user their guess is right
    print(f"Your guess is correct! Your guessed letter is at {found_position}!")
    #need to increment correct guess storage
    correct_guesses_storage += 1
    # tell user where their letters appeared
        # red-green-refactor ttd vibes, do for case of unique letters and then write loop
    if correct_guesses_storage == len(stored_word):
        print("You've won!")
        # how to end game?
        quit()
    # else:
        # run take user input for guess
    return