import random
import subprocess
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

ufo = '''
     ___
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
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
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
    if guesses_left > 1:
        for line in range(len(ASTRONAUT)):
            if 1 + lines_per_guess * (WRONG_GUESS_LIMIT - guesses_left) >= line:
                print(ASTRONAUT[line])
            # else:
                # print()
    else:
        for line in ASTRONAUT:
            print(line)


def update_wordbank(wordbank, letters_guessed):
    for letter in letters_guessed:
        wordbank.remove(letter)
    return wordbank


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
    wordbank = LETTER_BANK
    guesses_left = WRONG_GUESS_LIMIT
    playing = True

    # TODO: show the player information about the game according to the project spec
    print("* ~ * ~ * ~ * ~ * ~ * ~ * ~  SPACEMAN  ~ * ~ * ~ * ~ * ~ * ~ * ~ *")
    print("~ * ~ * ~ * Guess letters until you complete the word! * ~ * ~ * ~")
    print("~ * ~ * ~ * ~ * ~ * ~  You only have " + str(WRONG_GUESS_LIMIT) + " tries.  ~ * ~ * ~ * ~ * ~ * ~")

    while playing:

        # clear the screen and redraw the astronaut guy
        # subprocess.call('clear', shell=True)
        # load_ascii(guesses_left)
        print()

        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        while True:
            guessed_letter = input()
            if is_valid_guess(guessed_letter):
                if guessed_letter not in letters_guessed:
                    letters_guessed.append(guessed_letter)
                    break
                else:
                    print("You already tried this letter! Try again.")
            else:
                print("Please enter one letter.")

            #TODO: Check if the guessed letter is in the secret or not and give the player feedback


            #TODO: show the guessed word so far
        print(get_guessed_word(secret_word, letters_guessed))

            #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed):
            # "you win!" message goes here
            print("You win!")
            playing = False


# These function calls that will start the game
spaceman(load_word())
# play_again()
