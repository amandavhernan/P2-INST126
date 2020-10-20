#!/usr/bin/env python
# coding: utf-8

# In[ ]:


words = ["WHDSPQZ", "XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF", "XNOCFQGTM"]

import random 
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from the preselected list above
    
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 10
    
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters the player has already used, also shows how many lives they have left
        print('You have', lives,'lives left and you have used the following letters: ', ' '.join(used_letters))
        
        # what the current word is (ex A - A N - A for Amanda)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        # asks the user to guess a letter
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else: 
                lives = lives - 1 #takes a life away if user guesses an incorrect letter
                print('Sorry, the letter you guessed is not in the word.')
            
        elif user_letter in used_letters:
            print('You have already used that letter. Please choose a different letter and try again.')
        
        else:
            print('You have entered an invalid character. Please choose a letter and try again.')
        
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You have 0 lives left. The word was', word)
    else:
        print('You guessed the word', word,'correctly! Good job.')
        print('This was an encrypted word.')
        print('The decrypted word is', decrypt(word))
        
hangman()

# decrypts the encrypted word
def decrypt(ciphertext):
    plaintext = ""
    for i in range (0, len(ciphertext)):
        if 1 % 2 == 0: #even, -1
            plain_ascii = ciphertext[i]
            cipher_ascii = ord(plain_ascii) - 1
            plaintext = plaintext + str(chr(cipher_ascii))
        else: #odd, +1
            plain_ascii = ciphertext[i]
            cipher_ascii = ord(plain_ascii) + 1
            plaintext = plaintext + str(chr(cipher_ascii))
        
    return plaintext


# In[ ]:





# In[ ]:




