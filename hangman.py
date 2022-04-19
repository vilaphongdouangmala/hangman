# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_char_test = []
    for secret_char in secret_word:
        for guessed_char in letters_guessed:
            if secret_char == guessed_char:
                secret_char_test.append(secret_char)
                # secret_char = secret_char.replace(secret_char, "")
                break
    secret_char_test = "".join(secret_char_test)
    return secret_char_test == secret_word


#secret_word = "apple"
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_char_test = []
    for secret_char in secret_word:
        test = False
        for guessed_char in letters_guessed:
            if secret_char == guessed_char:
                secret_char_test.append(secret_char)
                test = True
                break
        if not test:
            secret_char_test.append("_ ")
    secret_char_test = "".join(secret_char_test)
    return secret_char_test


#secret_word = "apple"
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    english_letters = string.ascii_lowercase
    for guessed_char in letters_guessed:
        for english_char in english_letters:
            if guessed_char == english_char:
                english_letters = english_letters.replace(english_char, "")
                break
    return english_letters


#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    vowels = ['a', 'e', 'i', 'o', 'u']
    remaining_guesses = 6
    remaining_warnings = 3
    print("You have", remaining_warnings, "warnings left.")
    letters_guessed = []
    while remaining_guesses > 0:
        if not is_word_guessed(secret_word, letters_guessed):
            test = -1
            print("----------")
            print("You have", remaining_guesses, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            input_guessed = input("Please guess a letter: ").lower()
            for guessed_word in letters_guessed:
                if input_guessed == guessed_word:
                    test = 0
            letters_guessed.append(input_guessed)

            if test != 0:
                for secret_char in secret_word:
                    if input_guessed == secret_char:
                        test = 1
                        break
                if not input_guessed.isalpha():
                    if remaining_warnings > 0:
                        remaining_warnings -= 1
                        print("Oops! That is not a valid letter. You have", remaining_warnings, "warnings left.",
                              get_guessed_word(secret_word, letters_guessed))
                    else:
                        remaining_guesses -= 1
                        print("Oops! That is not a valid letter. You don't any warnings left. So you lose one guess.")
                elif test == 1:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                elif test == -1:
                    test2 = False
                    for v in vowels:
                        if v == input_guessed:
                            test2 = True
                            break
                    if not test2:
                        print("Oops! That's not in my word", get_guessed_word(secret_word, letters_guessed))
                        remaining_guesses -= 1
                    elif test2:
                        print("Oops! That's not in my word", get_guessed_word(secret_word, letters_guessed))
                        remaining_guesses -= 2
            if test == 0:
                if remaining_warnings > 0:
                    remaining_warnings -= 1
                    print("Oops! You have already guessed that letter. You have", remaining_warnings, "warnings left.",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    remaining_guesses -= 1
                    print("Oops! You have already guessed that letter. You don't any warnings left. "
                          "So you lose one guess.")
        else:
            print("----------")
            print("Congratulations, You won!!!")
            total_score = remaining_guesses * len(set(secret_word))
            print("Your Total Score for this game is", total_score)
            break
    else:
        print("----------")
        print("Sorry, You lost the game due to ran out of guesses.")
        print('The word was "'+secret_word+'"')


#secret_word = "task"
#hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    if len(my_word.replace(" ", "")) == len(other_word):
        i = 0
        test = True
        my_word = my_word.replace(" ", "")
        my_word = my_word + "#"
        while my_word[i] != "#":
            if my_word[i].isalpha():
                if my_word[i] == other_word[i]:
                    test = True
                else:
                    test = False
                    return test
            else:
                j = i
                my_word2 = my_word.replace("_", "")
                for myw2 in my_word2:
                    if other_word[j] == myw2:
                        test = False
                        return test
                test = True
            i += 1
        else:
            return test
    else:
        return False


#my_word = "a_ pl_ "
#other_word = "apply"
#print(match_with_gaps(my_word, other_word))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    test = False
    other_word2 = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            test = True
            other_word2.append(other_word)
    if test:
        other_word2 = " ".join(other_word2)
        print(other_word2)
    if not test:
        print("No matches found")


#my_word = "a_ pl_ "
#show_possible_matches(my_word)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    vowels = ['a', 'e', 'i', 'o', 'u']
    remaining_guesses = 6
    remaining_warnings = 3
    print("You have", remaining_warnings, "warnings left.")
    letters_guessed = []
    while remaining_guesses > 0:
        if not is_word_guessed(secret_word, letters_guessed):
            test = -1
            print("----------")
            print("You have", remaining_guesses, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            input_guessed = input("Please guess a letter: ").lower()
            for guessed_word in letters_guessed:
                if input_guessed == guessed_word:
                    test = 0
            letters_guessed.append(input_guessed)

            if test != 0:
                for secret_char in secret_word:
                    if input_guessed == secret_char:
                        test = 1
                        break
                if not input_guessed.isalpha():
                    if input_guessed == "*":
                        my_word = get_guessed_word(secret_word, letters_guessed)
                        print("Possible words are:")
                        show_possible_matches(my_word)
                    else:
                        if remaining_warnings > 0:
                            remaining_warnings -= 1
                            print("Oops! That is not a valid letter. You have", remaining_warnings, "warnings left.",
                                  get_guessed_word(secret_word, letters_guessed))
                        else:
                            remaining_guesses -= 1
                            print("Oops! That is not a valid letter. You don't any warnings left. So you lose one "
                                  "guess.")
                elif test == 1:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                elif test == -1:
                    test2 = False
                    for v in vowels:
                        if v == input_guessed:
                            test2 = True
                            break
                    if not test2:
                        print("Oops! That's not in my word", get_guessed_word(secret_word, letters_guessed))
                        remaining_guesses -= 1
                    elif test2:
                        print("Oops! That's not in my word", get_guessed_word(secret_word, letters_guessed))
                        remaining_guesses -= 2
            if test == 0:
                if remaining_warnings > 0:
                    remaining_warnings -= 1
                    print("Oops! You have already guessed that letter. You have", remaining_warnings, "warnings left.",
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    remaining_guesses -= 1
                    print("Oops! You have already guessed that letter. You don't any warnings left. "
                          "So you lose one guess.")
        else:
            print("----------")
            print("Congratulations, You won!!!")
            total_score = remaining_guesses * len(set(secret_word))
            print("Your Total Score for this game is", total_score)
            break
    else:
        print("----------")
        print("Sorry, You lost the game due to ran out of guesses.")
        print('The word was "' + secret_word + '"')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)