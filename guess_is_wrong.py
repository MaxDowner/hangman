
# would prefer a more functiony name
# could split into 2 for better naming
    # decrement_guesses()
    # check/exit_if_lost()
# or could just rename to decrement_allowed_guesses_and_check_if_lost
def guess_is_wrong(target_word: str, allowed_guesses: int) -> None:
    '''increments correct guesses and check if won'''
    print(f"Your guess is incorrect! You have {allowed_guesses} guesses left")
    allowed_guesses -= 1
    if allowed_guesses == 0:
        print("You've lost!")
        quit()
    return