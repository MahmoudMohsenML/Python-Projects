from colorama import Fore, Style
import os

# Initialize the board and winning lines
board = [str(i) for i in range(1, 10)]
winning_locations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def print_board():
    #Display the board with colored numbers.
    os.system('cls')  # Clear screen
    print("\n Tic-Tac-Toe Game \n")
    print(f"{Fore.BLUE}{board[0]} | {board[1]} | {board[2]}{Style.RESET_ALL}")
    print("---+---+---")
    print(f"{Fore.BLUE}{board[3]} | {board[4]} | {board[5]}{Style.RESET_ALL}")
    print("---+---+---")
    print(f"{Fore.BLUE}{board[6]} | {board[7]} | {board[8]}{Style.RESET_ALL}")

def is_valid_move(choice):
    # Check if the player's move is valid.
    try:
        choice = int(choice)
        if 1 <= choice <= 9 and board[choice - 1] not in ["X", "O"]:
            return True
        return False
    except ValueError:
        return False

def player_move(player):
    #Handle a player's move.
    while True:
        choice = input(f"Player {player}: Please enter the location number (1-9): ")
        if is_valid_move(choice):
            board[int(choice) - 1] = player
            break
        else:
            print("Invalid move! Choose an empty cell between 1 and 9.")

def check_winner():
    #Check if there's a winner or a tie.
    for loc in winning_locations:
        if board[loc[0]] == board[loc[1]] == board[loc[2]]:
            print(f"Player {board[loc[0]]} is the winner!")
            return True
    if all(cell in ["X", "O"] for cell in board):
        print("It's a tie!")
        return True
    return False

def play_game():
    #Main game loop.
    print_board()
    current_player = "X"
    while True:
        player_move(current_player)
        print_board()
        if check_winner():
            break
        current_player = "O" if current_player == "X" else "X"

def main():
    #Start the game and handle replay.
    while True:  
        global board
        board = [str(i) for i in range(1, 10)]  
        play_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()