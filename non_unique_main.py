from guess_is_right_non_unique import guess_is_right_non_unique
from guess_is_wrong import guess_is_wrong
from find_position_non_unique import find_position_non_unique
from word import word_input
from word import guesses

def main():
    target_word, allowed_guesses = word_input()
    list_of_chars = []
    while True:
        guesses()
        guessed_letter = list_of_chars[-1]
        # finish the found position_non_unque_function
        found_position = find_position_non_unique(target_word, guessed_letter)
         # potentially the logic behind the if/else statement
        if found_position == -1:
            guess_is_wrong(target_word, allowed_guesses)
        else:
            guess_is_right_non_unique(target_word, guessed_letter)
    return

# what's the __main__ thingy they usually do here
# do I need to do anything else