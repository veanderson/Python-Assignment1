#Number Game Guess
import random
secrete_number = random.randint(1,10)
print("Welcome to the guess number Game")
print("Try to guess thr number between 1 to 10")
guess = None

while guess != secrete_number:
    guess = int(input("Enter your guess"))
    if guess > secrete_number:
        print(f"Guess is toohigh! Try again")
    elif guess < secrete_number:
        print(f"{guess} is too low! Try again")
    else:
        print(f"Congratulation {guess} is the correct number")
    
