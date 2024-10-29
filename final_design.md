# Final Design Document


1. Start program
2. Important random Python function and set pre-game values
3. Define new_game():
   1. Ask for input of number of total sticks wanted (10-100)
   2. Check for misinput and repeat question if answer is wrong
   3. Output game start message
   4. While total amount of sticks is greater than zero:
      1. Start the game loop with a while statement (while sticks > 0:)
         1. Start of Player 1's turn
         2. Ask for input of Player 1's amount of sticks to take (1-3)
         3. If input is not 1-3, ask for reinput via while & if statement
         4. Subtract inpout amount from total sticks
         5. Check if Player 1 wins the game if total sticks <= 0
            1. Output win message for Player 1 if true
         6. Start of Player 2's turn
         7. Ask for input of Player 2's amount of sticks to take (1-3)
         8. If input is not 1-3, ask for reinput via while & if statement
         9. Subtract input amount from total sticks
         10. Check if Player 2 wins the game if total sticks <= 0
             1. Output win message for Player 2 if true
         11. Start of CPU's turn
         12. Pick a random integer from 1-3
         13. Output chosen integer ("CPU takes {cpu_sticks} sticks.")
         14. Subtract chosen integer from total sticks
         15. Ask the user input if they want to play again
         16. If input = "yes":
             1. Run new_game() function
             2. Else, output "Goodbye!"
4. Run new_game() function
