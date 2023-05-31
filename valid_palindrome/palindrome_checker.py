#!/usr/bin/env python3

def palin_maker(word):
    '''
    Find if a word can become a palindrome by removing at most 1 letter

    Args: 
        word (str): a given word

    Returns:
        String confirming if word is a palindrome or not and what the resulting palindrome is
    '''

    word = word.lower() # making lowercase

    if word == word[::-1]: return True, word # Testing if word is already a palindrome

    for i in range(len(word)): # Testing if word can be made into a palindrome
        test = str(word[:i]) + str(word[i+1:])
        if test == test[::-1]:
            return True, test

    return False, word 

def main():
    word = 'high'
    print({word: palin_maker(word)})



if __name__ == '__main__':
    main()

