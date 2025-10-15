def print_board(board):
    #print board
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(board):
    # check winners
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # return winner's symbol (X or O)
    return None

def is_board_full(board):
    #Check if the board is full
    return " " not in board

def get_player_move(board, player):
  #Get player's movement
    while True:
        try:
            move = int(input(f"please select a position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invaild! Please select a position that's not occupied (1-9)。")
        except ValueError:
            print("Invaild number！")

def play_tic_tac_toe():
    # initialize the map
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-tac-toe")
    print("Here's the map of the board：")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    
    while True:
        # display the board
        print_board(board)
        
        # get player movemenr
        move = get_player_move(board, current_player)
        board[move] = current_player
        
        # check winner condition
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Congrats to {winner} !")
            break
        
        # check tie condition
        if is_board_full(board):
            print_board(board)
            print("Game! Tied, haha")
            break
        
        # swap players
        current_player = "O" if current_player == "X" else "X"

def main():
    """主程序"""
    while True:
        play_tic_tac_toe()
        
        # ask if they wanna play again
        play_again = input("So do u wanna play again? (y/n): ").lower()
        if play_again != 'y':
            print("that sux, goodbye.")
            break

if __name__ == "__main__":
    main()
