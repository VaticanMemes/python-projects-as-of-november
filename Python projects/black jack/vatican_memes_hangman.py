"""
Full guy:
______
 |   0
 |  -|-
___ / |

Welcome to hangman! Would you like to play? (y/n) y
_ _ _ _ _
Enter a letter: E
______
 | 
 | 
___
Incorrect letters: E
_ _ _ _ _
Enter a letter: A
_ A _ _ _
"""
import random

WORDS = ['harry', 'barry', 'larry']
FIRST = ['______', '______', '______', '______', '______', '______', '______']
SECOND = [' |', ' |   0', ' |   0', ' |   0', ' |   0', ' |   0', ' |   0']
THIRD = [' |', ' |', ' |   |', ' |  -|', ' |  -|-', ' |  -|-', ' |  -|-']
FOURTH = ['___', '___', '___', '___', '___', '___ /', '___ / |']

def endgame(word):
    word = word
    print(f'You lose. The word was {word}.')

def loop(word, running_word, wrong, guessed_word, letters_chosen):
    word, running_word, wrong, guessed_word, letters_chosen = word, running_word, wrong, guessed_word, letters_chosen
    if wrong > 6:
        endgame(word)
    else:
        print(' '.join(guessed_word))
        letter = input('Enter a letter: ').lower()
        if len(letter) > 1:
            print('Please enter one character.')
            loop(word, running_word, wrong, guessed_word, letters_chosen)
        elif letter in letters_chosen:
            print(f'Already chosen "{letter}".')
            loop(word, running_word, wrong, guessed_word, letters_chosen)
        else:
            letters_chosen.append(letter)
            if letter in running_word:
                pass
            elif letter not in running_word:
                print(FIRST[wrong])
                print(SECOND[wrong])
                print(THIRD[wrong])
                print(FOURTH[wrong])
                print(f'Letters chosen: {", ".join(letters_chosen)}')
                wrong += 1
            else:
                print('Bug. Idk what happened here.')
            loop(word, running_word, wrong, guessed_word, letters_chosen)

def game():
    word = WORDS[random.randint(-1, (len(WORDS) - 1))]
    running_word = list(word)
    wrong = 0
    guessed_word = letters_chosen = []
    for i in running_word: 
        guessed_word.append('_')
    loop(word, running_word, wrong, guessed_word, letters_chosen)

def main():
    play_or_nay = input('Welcome to hangman! Would you like to play? (y/n) ')
    if play_or_nay == 'y':
        game()
    elif play_or_nay == 'n':
        quit()
    else:
        print("Please enter a valid function")
        main()

main()