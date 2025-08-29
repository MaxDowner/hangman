from guess_is_right import guess_is_right
from guess_is_wrong import guess_is_wrong
from find_position import find_position
from word import word_input
from word import guesses

def main():
    target_word, allowed_guesses = word_input()
    list_of_chars = []
    while True:
        guess()
        guessed_letter = list_of_chars[-1]
        found_position = find_position(target_word, guessed_letter)
        if found_position == -1:
            guess_is_wrong(target_word, allowed_guesses)
        else:
            guess_is_right(target_word, guessed_letter)
    return

# what's the __main__ thingy they usually do here
# do I need to do anything else