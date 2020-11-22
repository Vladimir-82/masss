import random

def display(HANGMAN_PICS, WORDS):

    choes = random.randint(0, len(WORDS) - 1)
    current_word = WORDS[choes]
    show_current_word = '*' * len(current_word)
    print(show_current_word)

    index_hangman = 0

    while '*' in show_current_word:

        current_letter = input('Введите букву:')
        if current_letter in current_word:
            index_letter=current_word.index(current_letter)
            show_current_word=show_current_word[0:index_letter:] + current_letter + show_current_word[index_letter+1::]
            print(show_current_word)
            if '*' not in show_current_word:
                print('YOU WON')

        else:
            print((HANGMAN_PICS[index_hangman]))
            if index_hangman==len(HANGMAN_PICS)-1:
                print('YOU LOST')
                break
            index_hangman+=1

WORDS = 'кот ёжик собака'.split()
HANGMAN_PICS=["""
 +---+
     |
     |
     |
    ===""", """
 +---+
 o   |
     |
     |
    ===""", """
 +---+
 o   |
 |   |
     |
    ===""", """
 +---+
 o   |
/|   |
     |
    ===""", """
 +---+
 o   |
/|\  |
     |
    ===""", """
 +---+
 o   |
/|\  |
/    |
    ===""", """
 +---+
 o   |
/|\  |
/ \  |
    ==="""]



print('Начнем!')
print()
display(HANGMAN_PICS, WORDS)

