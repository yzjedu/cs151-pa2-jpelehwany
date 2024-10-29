# Program written by John Elehwany
# Loyola CS151, Professor Zee
# October 23, 2024
# PA 02 Assignment

# This program is a game of sticks played by 2 players and one computer player.

# Import random Python and set pre-game values
import random

# Defines the amount of sticks to start with
def new_game():
    while True:
        try:
            sticks = int(input("Enter the number of sticks you want (10-100): "))
            if 10 <= sticks <= 100:
                break
            else:
                print("Invalid answer! Please input a number from 10-100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Outputs game start message
    print("""
    Let's begin!
    """)

    # Start of the game loop, kept in loop by making sure the total sticks are greater than zero
    while sticks > 0:
        print(f"Total sticks remaining: {sticks}")

        # Start of Player 1's move
        while True:
            try:
                player1_sticks = int(input("Player 1, it's your turn! How many sticks do you want? (1-3): "))
                if 1 <= player1_sticks <= 3:
                    sticks -= player1_sticks
                    break
                else:
                    print("Invalid answer! Please input a number between 1-3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Checks if Player 1 wins the game
        if sticks <= 0:
            print("Player 1 wins the game!")
            break

        # Start of Player 2's move
        print(f"\nTotal sticks remaining: {sticks}")
        while True:
            try:
                player2_sticks = int(input("Player 2, it's your turn! How many sticks do you want? (1-3): "))
                if 1 <= player2_sticks <= 3:
                    sticks -= player2_sticks
                    break
                else:
                    print("Invalid answer! Please input a number between 1-3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Checks if Player 2 wins the game
        if sticks <= 0:
            print("Player 2 wins the game!")
            break

        # Start of CPU's move
        print(f"Sticks remaining: {sticks}")
        cpu_sticks = random.randint(1, 3)
        print(f"CPU takes {cpu_sticks} sticks.")
        sticks -= cpu_sticks

        # Checks if CPU wins the game
        if sticks <= 0:
            print("CPU wins the game!")
            break

    # Asks the user if they want to play again
    replay = input("Do you want to play again? (yes/no)")
    if replay == 'yes':
        new_game()
    else:
        print("Goodbye!")

# The game starts with running the defined function
new_game()
