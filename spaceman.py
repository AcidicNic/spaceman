import random
import subprocess
import sys
from builtins import len, range

WRONG_GUESS_LIMIT = 7

LETTER_BANK = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# found the art here https://www.asciiart.eu/space
ASTRONAUT = [ # 1 + (WGL - GL)*2
    "        _..._",
    "      .'     '.      _",#7 -2
    "     /    .-\"\"-\\   _/ \\",
    "   .-|   /:.   |  |   |",#6 -4
    "   |  \\  |:.   /.-'-./",
    "   | .-'-;:__.'    =/",#5 -6
    "   .'=  *=|NASA _.='",
    "  /   _.  |    ;",#4 -8
    " ;-.-'|    \\   |",
    "/   | \\    _\\  _\\",#3 -10
    "\\__/'._;.  ==' ==\\",
    "         \\    \\   |",#2 -12
    "         /    /   /",
    "         /-._/-._/",#1 -14
    "  jgs    \\   `\\  \\",
    "          `-._/._/"#0 gameover -16
]

ufo = '''     ___
 ___/   \\___
/   '---'   \\
'--_______--'
     / \\
    /   \\
    /\\O/\\
    / | \\
    // \\\\
'''


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the
    secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed
        correctly, the string shouldcontain the letter at the correct position.
        For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    output = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output += letter
        else:
            output += "_"
    return output


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    if guess in secret_word:
        return True
    return False


def load_ascii(guesses_left):
    '''

    :param guesses_left:
    :return:
    '''

    lines_per_guess = len(ASTRONAUT)/WRONG_GUESS_LIMIT
    if guesses_left > 0:
        for line in range(len(ASTRONAUT)):
            if lines_per_guess * (WRONG_GUESS_LIMIT - guesses_left) >= line:
                print(ASTRONAUT[line])
    else:
        for line in ASTRONAUT:
            print(line)


def update_wordbank(word_bank, letters_guessed):
    for letter in letters_guessed:
        if letter.upper() in word_bank:
            word_bank.remove(letter.upper())
    return word_bank


def is_valid_guess(guessed_letter):
    if len(guessed_letter) == 1 and guessed_letter.isalpha():
        return True
    return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    letters_guessed = []
    global WRONG_GUESS_LIMIT
    WRONG_GUESS_LIMIT = len(secret_word)
    wordbank = LETTER_BANK.copy()
    guesses_left = WRONG_GUESS_LIMIT
    playing = True

    # TODO: show the player information about the game according to the project spec
    print("* ~ * ~ * ~ * ~ * ~ * ~ * ~  SPACEMAN  ~ * ~ * ~ * ~ * ~ * ~ * ~ *")
    print("~ * ~ * ~ * Guess letters until you complete the word! * ~ * ~ * ~")
    print("~ * ~ * ~ * ~ * ~ * ~  You only have " + str(WRONG_GUESS_LIMIT) + " tries.  ~ * ~ * ~ * ~ * ~ * ~")

    print(get_guessed_word(secret_word, letters_guessed))


    while playing:

        # clear the screen and redraw the astronaut guy
        # subprocess.call('clear', shell=True)
        # load_ascii(guesses_left

        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        while True:
            guessed_letter = input("Guess: ")
            if is_valid_guess(guessed_letter):
                if guessed_letter not in letters_guessed:
                    letters_guessed.append(guessed_letter)
                    break
                else:
                    print("You already tried this letter! Try again.")
            else:
                print("Please enter one letter.")

        wordbank = update_wordbank(wordbank, letters_guessed)

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guessed_letter, secret_word):
            print("Correct!")
        else:
            guesses_left -= 1
            load_ascii(guesses_left)
            print("Wrong. Your have " + str(guesses_left) + " tries left")
            print("Unused letter: " + ', '.join(wordbank))

        #TODO: show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))

        #TODO: check if the game has been won or lost
        if guesses_left == 0:
            print("You ran out of guesses! Game over.")
            print("The word was " + secret_word)
            playing = False
        if is_word_guessed(secret_word, letters_guessed):
            print(ufo)
            print("   You win!")
            playing = False

    response = input("\n\nWould you like to play again? (y to continue): ")
    if response.lower() == 'y' or response.lower() == "yes":
        print("New game starting...")
    else:
        print(ufo)
        print("Goodbye!")
        sys.exit()


# These function calls that will start the game
while True:
    playing = spaceman(load_word())


#TODO - print wordbank; print astronaut;
