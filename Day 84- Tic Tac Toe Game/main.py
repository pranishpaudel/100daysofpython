import random

def print_board(board):
    header = "   " + "   ".join(str(i) for i in range(len(board)))
    print(header)
    print("  " + " " + "-" * (4 * len(board[0]) - 1))
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        if i != len(board) - 1:
            print("  " + "-" * (4 * len(row) - 1))

# Example board
tic_tac_toe_board = [
    ["N1", "N2", "N3"],
    ["N4", "N5", "N6"],
    ["N7", "N8", "N9"]
]

def check_match_of_line(now_option):
    if tic_tac_toe_board[0][0] == now_option and tic_tac_toe_board[0][1] == now_option and tic_tac_toe_board[0][2] == now_option:
        return True
    elif tic_tac_toe_board[1][0] == now_option and tic_tac_toe_board[1][1] == now_option and tic_tac_toe_board[1][2] == now_option:
        return True
    elif tic_tac_toe_board[2][0] == now_option and tic_tac_toe_board[2][1] == now_option and tic_tac_toe_board[2][2] == now_option:
        return True
    elif tic_tac_toe_board[0][0] == now_option and tic_tac_toe_board[1][0] == now_option and tic_tac_toe_board[2][0] == now_option:
        return True
    elif tic_tac_toe_board[0][1] == now_option and tic_tac_toe_board[1][1] == now_option and tic_tac_toe_board[2][1] == now_option:
        return True
    elif tic_tac_toe_board[0][2] == now_option and tic_tac_toe_board[1][2] == now_option and tic_tac_toe_board[2][2] == now_option:
        return True
    elif tic_tac_toe_board[0][0] == now_option and tic_tac_toe_board[1][1] == now_option and tic_tac_toe_board[2][2] == now_option:
        return True
    elif tic_tac_toe_board[0][2] == now_option and tic_tac_toe_board[1][1] == now_option and tic_tac_toe_board[2][0] == now_option:
        return True
    else:
        return False
     
     


IS_GAME_STARTED=False

TIC_TAC_TOE_OPTIONS= ["X","O"]
TIC_TAC_TOE_OPTIONS_COUNTS= [0,0]

def print_the_turn(char):
    print(f"Its {char}'s turn now")
# Print the Tic Tac Toe board
print_board(tic_tac_toe_board)
right_now_option_value=0

print("\nHello welcome to Tic Tac Toe Game! Its me Pranish Here to Guide You!!!")
print("\nN in the rows represent null values for now which will be filled upon your choice")
first_user_choice= input("\nIts a two player game so please choose your patner to start the Game: Send 'DONE' to start")

if  first_user_choice.lower()=="done":
    IS_GAME_STARTED=True
    while IS_GAME_STARTED:
        now_option=TIC_TAC_TOE_OPTIONS[right_now_option_value]
        user_choice_now= print(f"Where do you want to put the bet player {now_option}??")
        user_row_now= int(input("Enter the row index?"))-1
        user_column_now= int(input("Enter the column index?"))-1
        row_to_update= tic_tac_toe_board[(user_row_now)]
        column_to_print= row_to_update[(user_column_now)]
        if not column_to_print=="O" and not column_to_print=="X":
            if not TIC_TAC_TOE_OPTIONS_COUNTS[right_now_option_value]==3:
                row_to_update[user_column_now]=TIC_TAC_TOE_OPTIONS[right_now_option_value]
                TIC_TAC_TOE_OPTIONS_COUNTS[right_now_option_value]+=1
                print_board(tic_tac_toe_board)
                print(TIC_TAC_TOE_OPTIONS_COUNTS)
                if check_match_of_line(now_option)==True:
                     print(f"Player {now_option} wins")
                     IS_GAME_STARTED=False

                if right_now_option_value==0:
                        right_now_option_value=1
                else:
                        right_now_option_value=0
            elif TIC_TAC_TOE_OPTIONS_COUNTS[0]==3 and TIC_TAC_TOE_OPTIONS_COUNTS[1]==3:
                 print(f"The game is a draw")
                 IS_GAME_STARTED=False
            else:
                 print(f"The player {now_option} all 3 tries reached")
                 IS_GAME_STARTED=False
        else:
             print("You cant update the column that already has other player's value")









