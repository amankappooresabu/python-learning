import random

words = ['python', 'java', 'kotlin', 'javascript']

hangman_art = {0 : '',
               1 : 'o',
               2 : ('o',
                    '|'),
               3 : ('o',
                    '|',
                    '|')}

def display_art(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
def display_answer(answer):
    for i in answer:
        print(i, end=' ')
def main():
    wrong_guesses = 0
    is_running = True
    answer = random.choice(words)
    hint = ['_']*len(answer)
    while is_running:
        print('Welcome to Hangman!')
        display_art(wrong_guesses)
        for i in hint:
            print(i, end=' ')
        print()
        guess = input('Enter your guess :')
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        if len(guess) > 1 or guess.isalpha() == False:
            print('Invalid input')
            continue        
        if guess not in answer:
            wrong_guesses += 1    
        if wrong_guesses == 3:
            display_art(wrong_guesses)
            print('You lost')
            is_running = False
        if answer == ''.join(hint):
            display_answer(answer)
            print('\nYou won!')
            is_running = False  
                    
        
        

if __name__ == '__main__':
    main()