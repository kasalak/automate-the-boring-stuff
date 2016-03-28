import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20."
)

#player guesses
for guessesTaken in range(1, 7):
    print ('Guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is lower than my number. Try again')
    elif guess > secretNumber:
        print('Your guess is higher than my number. Try again')
    elif guess == secretNumber:
        print('Congratulations, you guessed my number! It took you {} tries!'.format(str(guessesTaken)))
        break
