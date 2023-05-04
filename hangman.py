import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        print(f'Remaining lives: {lives}')
        if len(guessed_letters) > 0:        
            print('You have already guessed these letters: ', ' '.join(guessed_letters))
        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print('Current word state:',' '.join(word_list))
              
        user_guess = input('Guess a letter: ').upper()
        if  user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
            
            else:
                lives -= 1
                

        elif user_guess in guessed_letters:
            print(f'Already guessed {user_guess}')

        else:
            print('Invalid guess')
            
    if lives == 0:
        print(f'Oh no, you died :( ~~ The word was {word}')
    else:
        print(f'Yay you guessed {word}!')

hangman()
    
