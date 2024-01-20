import random

def guess_number_game():
    print("Guess the correct number between 1 to 50")
    
    # n is the number of guesses each user gets
    n = random.randint(3, 5)
    # random number generated 
    random_number = random.randint(1, 50)
    
    print(f"You have {n} chances to guess the correct number")

    while True:
        guessed_number = int(input("Let's see if you can guess: "))
        
        # Check if the guessed number is in the valid range
        if guessed_number < 1 or guessed_number > 50:
            print("Please enter a number between 1 to 50")
            continue

        # Check if the guessed number is too high, too low, or correct
        if guessed_number > random_number:
            print("Oops, too high!")
        elif guessed_number < random_number:
            print("Oops, too low :(")
        else:
            print("Yay! You guessed the correct number :)")
            break

        n -= 1
        print(f"You have {n} more chances left")

        # Check if the user has run out of chances
        if n == 0:
            print("Oops! You have zero chances left")
            print("Sorry, you lost the game :(")
            break

    play_again = input("Do you want to play again? (y/n): ")
    
    if play_again.lower() == "y":
        guess_number_game()
    else:
        print("Thank you for playing")
        print("Be well :)")

# Call the function to start the game
guess_number_game()
