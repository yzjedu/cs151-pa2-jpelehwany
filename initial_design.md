# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

1. Start program
2. Ask for user input of how many stick they want (How many sticks do you want? (10-100))
   1. Check for mis-input and loop if input is incorrect
3. Define variables P1, P2, and CPU
4. Output game start
5. Def game:
5. While total_sticks > 0:
6. Create a loop of game steps counting as turns
    1. Loop displays amount of sticks (total_sticks)
   2. Ask for Player 1's input of how many sticks they will take
      1. Loop if misinput and check if between 1-3
   3. Ask for Player 2's input of how many sticks they will take
      1. Loop if misinput and check if between 1-3
   4. Generate amount of sticks for CPU to take
   5. Output CPU's taken value
7. Take inputs from stick count and subtract them from total_sticks value
8. Run game
9While total_sticks <= 0:
10Output results of game; output winner
11. Ask if they want to play again
    1. If yes:
       1. Re-run game via running def 
    2. If no:
       1. Do nothing (end script)