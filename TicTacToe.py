from helpers import draw_board, check_turn, check_for_win
import os

# Initialize the game board with numbered spots
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

# Function to clear the console screen
def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

# Function to check if the board is full
def is_board_full(spots):
    return all(spot in {'X', 'O'} for spot in spots.values())

# Main game loop
playing = True
turn = 0

while playing:
    clear_screen()  # Clear the screen at the start of each turn
    draw_board(spots)  # Draw the current state of the board
    
    # Determine and print whose turn it is
    if turn % 2 == 0:
        print("Player 1's turn (X).")
        current_player = 'X'
    else:
        print("Player 2's turn (O).")
        current_player = 'O'
    
    choice = input("Choose a position (1-9) or 'q' to quit: ")
    if choice == 'q':
        playing = False
    elif choice.isdigit() and int(choice) in spots:
        if spots[int(choice)] not in {'X', 'O'}:
            spots[int(choice)] = current_player
            turn += 1  # Increment turn after a successful move
            
            # Check for a win after the move
            if check_for_win(spots):
                clear_screen()
                draw_board(spots)
                print(f"Congratulations! Player {current_player} wins!")
                print("Thanks for playing!")
                if input("Rematch? (Y/N): ").upper() == 'Y':
                    spots = {i: str(i) for i in range(1, 10)}
                    turn = 0
                    continue
                else:
                    break
        else:
            print("This spot is already taken. Please choose another spot.")
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
        
    # Check for tie
    if not check_for_win(spots) and is_board_full(spots):
        print("It's a tie!")
        if input("Rematch? (Y/N): ").upper() == 'Y':
            spots = {i: str(i) for i in range(1, 10)}
            turn = 0
            continue
        else:
            print("Thanks for playing!")
            break
