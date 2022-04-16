import random
secretNum=random.randint(1,100)                                                      #generate a random number between [1 100]
guessNum=int(input("Guess a number between 1 and 100 inclusive:"))
while guessNum != secretNum :
    if guessNum<secretNum :
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guessNum=int(input("Guess a number between 1 and 100 inclusive:"))
print("Congratulations! You guessed the number correctly.")
