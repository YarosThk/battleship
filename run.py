import string
from main import Game, Board, Player


rows = 10
columns = 10
ship_type = ["Carrier" , "Battleship", "Cruiser", "Submarine", "Destroyer"]
ships_settings = {"Carrier": 5 , "Battleship" : 4, "Cruiser" : 3, "Submarine" : 3, "Destroyer" : 2}


computer_ships = {"Carrier": [(4, 5), (4, 6), (4, 4), (4, 3), (4, 2)],
                "Battleship" : [(1, 10), (2, 10), (3, 10), (4, 10)],
                "Cruiser" : [(8, 1), (9, 1), (10, 1)],
                "Submarine" : [(7, 5), (7, 6), (7, 7)],
                "Destroyer" : [(9,8), (9,9)]}

player_ships = {"Carrier": [(2, 5), (2, 6), (2, 4), (2, 3), (2, 2)],
                "Battleship" : [(1, 8), (2, 8), (3, 8), (4, 8)],
                "Cruiser" : [(10, 2), (10, 3), (10, 4)],
                "Submarine" : [(7, 7), (8, 7), (9, 7)],
                "Destroyer" : [(10,9), (10,10)]}

for_auto_input = [computer_ships, player_ships]

def main():
    game = Game()
    player = Player('Boii')
    computer = Player("Spoink")
    player_board = Board(rows, columns, player.name)
    computer_board = Board(rows, columns, computer.name)


    player_board.render_board()
    player.define_ships(player_board, ships_settings)

    print(player.player_ships)




if __name__ == "__main__":
    #main()
    game = Game()
    player = Player('Boii')
    computer = Player("Spoink")
    player_board = Board(rows, columns, player.name)
    computer_board = Board(rows, columns, computer.name)


    player.auto_boat_input(player_ships, player_board)
    computer.auto_boat_input(computer_ships, computer_board)
    print(player.player_ships)
    print(computer.player_ships)
    player_board.render_board()
    computer_board.render_board()
