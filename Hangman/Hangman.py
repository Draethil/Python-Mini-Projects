import random
from words import words
import string

def get_valid_words():
    word = random.choice(words) # Choose a random word

    while '-' in word or ' ' in word: # Word shouldn't contain '-' or blank character
        word = random.choice(words)
    
    return word.upper() # Guessing only Upper Letters

def hangman():
    word = get_valid_words()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    player_lives = 8

    while len(word) > 0 and player_lives > 0:
        # Print out which letters the user already used and how many player lives are left
        print('You have', player_lives,' lives left and you have used these letters: ', ' '.join(used_letters))

        # Print out your current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_guess = input('Guess a letter: ').upper()
        if user_guess in alphabet - used_letters: # guessed character in alphabet
            used_letters.add(user_guess)
            if user_guess in word_letters: # guessed character in chosen word
                word_letters.remove(user_guess)
                print('')
            else:
                player_lives = player_lives - 1    

        elif user_guess in used_letters:
            print ('\n You have already used that letter. Guess another letter.')

        else: 
            print ('\n That is not a valid letter.')

    if player_lives == 0:
        print('You lost! The word was: ', word)
    elif len(word):
        print('You won! The word was ', word, '!')

if __name__ == '__main__':
    hangman()