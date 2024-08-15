import random

print("Welcome to the Number Game!")
print("Guess the number between 1 and 100.")

number = random.randint(1, 100)  
guess = -1  
while guess != number:
    guess_str = input("Enter your guess: ")
    guess = int(guess_str)

    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")

print(f"Well Done! You guessed the number {number} correctly!")
