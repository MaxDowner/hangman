# would prefer a more functiony name
# could split into 2 for better naming
    # increment__correct_guesses()
    # exit/check_if_won()
# or could just rename to increment_correct_guesses_and_check_if_won
def guess_is_right_non_unique(found_position: list, target_word: str) -> None:
    '''increment_correct_guesses_and_check_if_won'''
    print(f"Your guess is correct! Your guessed letter(s) is at {found_position}!")
    correct_guesses += len(found_position)
    if correct_guesses == len(target_word):
        print("You've won!")
        quit()
    return