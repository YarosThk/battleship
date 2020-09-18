import string
import random
from main import Game, Board, Player


rows = 10
columns = 10
ships_settings = {"Carrier": 5 , "Battleship" : 4, "Cruiser" : 3, "Submarine" : 3, "Destroyer" : 2}


#only use in auto_boat_input for quick testing.
#You can put as many ships as you want, even just one or two ships.
player_ships = {"Carrier": [(2, 5), (2, 6), (2, 4), (2, 3), (2, 2)],
                "Battleship" : [(1, 8), (2, 8), (3, 8), (4, 8)],
                "Cruiser" : [(10, 2), (10, 3), (10, 4)],
                "Submarine" : [(7, 7), (8, 7), (9, 7)],
                "Destroyer" : [(9,8), (9,9)]}

player2_ships = {"Carrier": [(3, 5), (3, 6), (3, 4), (3, 3), (3, 2)],
                "Battleship" : [(2, 8), (3, 8), (4, 8), (5, 8)],
                "Cruiser" : [(8, 1), (9, 1), (10, 1)],
                "Submarine" : [(1, 5), (1, 6), (1, 7)],
                "Destroyer" : [(6,8), (6,9)]}


def battleship():
    '''
        Functions that set ups the game and runs it.
    '''
    game = Game()
    player = Player()
    player2 = Player()

    player_board = Board(rows, columns)
    player_tracking = Board(rows, columns) #board to mark shots
    player2_board = Board(rows, columns)
    player2_tracking = Board(rows, columns) #board to mark shots


    '''
        Comment out (#) player.define_ships, and uncomment player.auto_boat_input
        to automate ta ships set up for quick testing. Leave player2.auto_boat_input
        as is.
    '''
    player.define_ships(player_board, ships_settings)
    #player.auto_boat_input(player_ships, player_board)
    player2.auto_boat_input(player2_ships, player2_board)


    #turn taking
    turn = 1
    while True:
        print("\n"*5)
        if turn == 1: #player1 turn
            print(f"{player.name}'s MOVE")

            print(f"{player.name}'s TRACKING BOARD")
            player_tracking.render_board()

            print(f"{player.name}'s PRIMARY BOARD")
            player_board.render_board()

            player.perform_shot(player_tracking, player2_board, player2.player_ships)
            #player_tracking.render_board()

            if Game.player_status(player2.player_ships):
                print(f"GAME OVER, {player.name} WINS")
                break

            turn -= 1

        elif turn == 0: #player2 round
            print(f"{player2.name}'s move")

            player2.perform_shot(player2_tracking, player_board, player.player_ships, Game.machine_move())
            #player2_tracking.render_board()

            if Game.player_status(player.player_ships):
                print(f"GAME OVER, {player2.name} WINS")
                break
            turn += 1


if __name__ == "__main__":
    battleship()
    '''
    FOR THE NEXT RUN REMEMBER TO RECORD AND RETURN (PRINT) ALL PLAYER MOVES TO
    CHECK IF COMPUTER HAS THE SAME AMOUNT OF MOVES RECORDED AS THE PLAYER.

    Analyse the control flow when computer repeats random choice!
    '''
