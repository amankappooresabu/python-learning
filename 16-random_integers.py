import random

low = 1
high = 100
answer = random.randint(low,high)
guesses = 0

print('Welcome to python guessing game')

print(f'Select a number between {low} and {high}')
while True :
    guess = (input('Enter your guess : '))
    guesses += 1
    if guess.isalpha():
        print('Please enter a valid number')
    elif int(guess) < answer:
        print('Too low')
    elif int(guess) > answer:
        print('Too high')
    elif int(guess) == answer:
        print('Correct')
        break

print(f" The answer was {guess}")
print(f"You took {guesses} guesses")

options = ('rock','paper','scissors')

while True:
    computer = random.choice(options)

    player = input('Enter your choice : ')

    print(f"Player choice : {player}")
    print(f"Computer choice : {computer}")

    if player == computer:
        print('It is a tie')
    elif player == 'rock' and computer == 'scissors':
        print('You win')
    elif player == 'paper' and computer == 'rock':
        print('You win')
    elif player == 'scissors' and computer == 'paper':
        print('You win')
    else:
        print('You lose')
    if print(input('Play again ? ').lower()) != 'yes':
        break
    



