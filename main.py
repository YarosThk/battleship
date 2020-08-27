import re
import string

class Game:
    def __init__(self):
        # self.player_name = input("Player name: ")
        # self.computer_name = "Spoink"
        self.player_points = 0
        self.computer_points = 0

    @staticmethod
    def check_input(inpt):
        '''
            Checks if input is as expected
        '''
        if re.match("^\((?:[1-9]|0[1-9]|10),\s{0,1}(?:[1-9]|0[1-9]|10)\)$", str(inpt)):
            return True
        else:
            return False

    @staticmethod
    def check_membership(coord, player_ships):
        '''
            Checks if coordinate has not been used already for other ships
        '''
        if any(coord in ship for ship in player_ships.values()):
            return False #meaning coordinate already exists
        else:
            return True

    @staticmethod
    def check_distance(coords):
        '''
            Checks distance and slope between points to assert correct coordinates
        '''
        ordered = sorted(coords)
        if len(coords) > 1:
            manhattan = abs(ordered[0][0] - ordered[-1][0]) + abs(ordered[0][1] - ordered[-1][1])
            if manhattan == len(coords)-1:
                try:
                    slope = (ordered[-1][1] - ordered[0][1]) / (ordered[-1][0] - ordered[0][0])

                except ZeroDivisionError:
                    #print("X is zero, need to check if manhattan distance is equal to 1")
                    print(f"Slope gives error and manhattan is {manhattan}")
                    return True

                else:
                    if slope == 0:
                        print(f"Slope is {slope} and manhattan is {manhattan}")
                        return True

                    else:
                        print(slope)
                        return False

            else:
                print(f"Manhattan distance is not correct")
                return False
        else:
            return True



class Board:

    def __init__(self, columns, rows, player_name):
        self.rows = rows
        self.columns = columns
        self.board_array = self.board_array(self.rows, self.columns)
        self.player_name = player_name

    def board_array(self, rows, columns):
        '''
            Creates the layout of the table
        '''
        board_array = []
        board_array.append(list(" "))
        board_array[0].append(" ".join(map(str, list(range(1, columns+1)))))
        for i in range(1, rows+1): #need to add +1 because one row in the board_array belong to ascii characters
            board_array.append(list((f"{ i }", " ".join(" " * rows))))
        return board_array

    def render_board(self):
        '''
            Will render the state of a player's board
        '''
        print(f"{self.player_name}'s' board. ")
        for r in self.board_array:
            print(r)

    def set_pegs(self, ship):
        '''
            Set's player's pegs on the board to show boats
        '''
        for p in ship:
            pos = list(self.board_array[p[1]][1][::2])
            pos[p[0]-1] = "#"

            pos = " ".join(pos)

            self.board_array[p[1]][1] = pos

        self.render_board()

    def paint_shot(self, ships, shot):
        '''
            Marks * or @ is hit or miss respectively
        '''
        #shot = shot[0]
        if shot in ships:
            print(f"HIT on {shot}")
            pos = list(self.board_array[shot[1]][1][::2])
            pos[shot[0]-1] = "*"
            pos = " ".join(pos)
            self.board_array[shot[1]][1] = pos
            self.render_board()

        else:
            print("MISS")
            pos = list(self.board_array[shot[1]][1][::2])
            pos[shot[0]-1] = "@"
            pos = " ".join(pos)
            self.board_array[shot[1]][1] = pos
            self.render_board()



class Player:

    def __init__(self, name):
        self.name = name
        self.player_ships = {}

    def define_ships(self, player_board, ships_settings):

        for s, l in ships_settings.items():
            temp_coordinates = []
            for n in range(l):
                while True:
                    print(f"Insert one coordinate at a time (eg: 1, 1) for each cell in : {s}")
                    print(f"{n} out of {l}")
                    try:
                        coordinate = tuple(map(int, input().split(",")))
                        if Game.check_input(coordinate):
                            if Game.check_membership(coordinate, self.player_ships):
                                temp_coordinates.append(coordinate)
                                if Game.check_distance(temp_coordinates):
                                    break
                                else:
                                    temp_coordinates.pop()
                                    print("Invalid distance between coordinates")
                                    continue
                            else:
                                print("Coordinate already assigned to another ship")
                                continue
                        else:
                            print("Wrong input", coordinate)
                            continue #will redirect to while loop
                    except (ValueError, ValueError):
                        print(f"Inser comma separated integers. Value is not valid")

                self.player_ships[s] = temp_coordinates
            print("Setting pegs")
            player_board.set_pegs(self.player_ships[s])

    def perform_shot(self, target_board):
        while True:
            print(f"Insert one coordinate (eg: 1, 1) to perform a shot")
            try:
                coordinate = tuple(map(int, input().split(",")))
                if Game.check_input(coordinate):
                    target_board.paint_shot(self.player_ships["Carrier"], coordinate)

            except (ValueError, ValueError):
                print(f"Inser comma separated integers. Value is not valid")


    def auto_boat_input(self, ships, player_board):
        '''
            Methods to automatically input boats for testing the game quicker
        '''
        self.player_ships = ships

        for s, l in ships.items():
            player_board.set_pegs(self.player_ships[s])


if __name__ == "__main__":

    rows = 10
    columns = 10
    ship_type = ["Carrier" , "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ships_settings= {"Carrier": 5 , "Battleship" : 4, "Cruiser" : 3, "Submarine" : 3, "Destroyer" : 2}
