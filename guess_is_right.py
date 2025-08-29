# would prefer a more functiony name
# could split into 2 for better naming
    # increment__correct_guesses()
    # exit/check_if_won()
# or could just rename to increment_correct_guesses_and_check_if_won
def guess_is_right(found_position: str, target_word: str) -> None:
    '''increment_correct_guesses_and_check_if_won'''
    print(f"Your guess is correct! Your guessed letter is at {found_position}!")
    correct_guesses += 1
    # tell user where their letters appeared
        # red-green-refactor ttd vibes, do for case of unique letters and then write loop
    if correct_guesses == len(target_word):
        print("You've won!")
        quit()
    return