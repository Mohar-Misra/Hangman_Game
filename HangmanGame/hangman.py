import random
import string
from wordlist import wordlist # imported the list of words from wordlist.py

def get_valid_word(wordlist):
    random_word = random.choice(wordlist) #randomly chooses something from that list
    while '-' in wordlist or ' ' in wordlist:
        random_word = random.choice(wordlist)
    return random_word.upper()

def hangman():
    random_word = get_valid_word(wordlist) #Stores the random word returned from the top function
    word_letters = set(random_word)
    word_length = len(random_word) #length of the word
    letter_bank = set(string.ascii_uppercase) #All english alphabets in uppercase
    chosen_letter = set() #Choosen letters by the user
    #getting user input
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(chosen_letter))

        #shows the current progress of the guessed word
        word_list = [letter if letter in chosen_letter else '-' for letter in random_word]
        print('Current progress is: ', ' '.join(word_list))

        guess_letter = input('Guess the letter: ').upper()
        if guess_letter in letter_bank - chosen_letter: # Checks if guessed letter is in the difference of letterbank and chosen letter
            chosen_letter.add(guess_letter)
            # Checks if the guessed word is in the random word. Checks if the guessed letter is already chosen or not.
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)


        elif guess_letter in chosen_letter:
                print('You have already chosen it.')
                print(" ")
        else:
            print('Invalid input')
            print(" ")
        print(" ")
    word_list = [letter if letter in chosen_letter else '-' for letter in random_word]
    print(word_list)
hangman()

