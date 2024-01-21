
#Activity "Guess the number"
import random
number = random.randint(1, 100)
number_of_guesses = 0
number_of_chances = 20
while number_of_guesses < number_of_chances:
    print('Guess a number between 1 and 100:')
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print("Whoo! That's the magic number!")
        break
    print(f"Darn, that wasn't the right number. You have {number_of_chances - number_of_guesses} chances left to guess the magic number!")
print(f"Aww, you ran out of guesses. The magic number was {number}.")
