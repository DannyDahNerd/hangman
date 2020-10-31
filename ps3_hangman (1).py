# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    FalseScore = 0
    TrueScore = 0
    for i in range(len(secretWord)):
        if (secretWord[i] in lettersGuessed) == False:
            FalseScore += 1
            break
        elif (secretWord[i] in lettersGuessed) == True:
            TrueScore += 1
    if (FalseScore == 0 and TrueScore > 0):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word += secretWord[i]
        else:
            word += '_ '
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    AvailableLetters = ''
    for i in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] not in lettersGuessed:
            AvailableLetters += string.ascii_lowercase[i]
    return AvailableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    GuessesLeft = 8
    lettersGuessed = []
    
    print('Hello! Welcome to hangman!')
    print('The word I\'m thinking of has', len(secretWord), 'letters long.')
    while GuessesLeft > 0:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
                print('--------------------------')
                return print('Congratulations, you won!')
                break
        print('--------------------------')
        print('You have', GuessesLeft, 'guesses left.')
        print('Available Letters:', getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter:").lower()
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            GuessesLeft -= 1
    if GuessesLeft == 0:
        print('--------------------------')
        return print('Sorry, you ran out of guesses. The word was ',secretWord,'.',sep='')
        
    
            
        
            
        
        
        
    







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)