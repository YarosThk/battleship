import re
import string
import random

class Game:
    @staticmethod
    def check_input(inpt):
        '''
            Checks if input is as expected
        '''
        if re.match("^\((?:[1-9]|0[1-9]|10),\s{0,1}(?:[1-9]|0[1-9]|10)\)$", str(inpt)):
            return True
        else:
            print("Only integers between 1-10 are valid!")
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
                    #print(f"Slope gives error and manhattan is {manhattan}")
                    return True

                else:
                    if slope == 0:
                        #print(f"Slope is {slope} and manhattan is {manhattan}")
                        return True

                    else:
                        #print(slope)
                        return False

            else:
                #print(f"Manhattan distance is not correct")
                return False
        else:
            return True

    @staticmethod
    def delete_boat_pos(coordinate, target_ships):
        '''
            Eliminates a boat from players ships to measure when hit or hit &
            sunk, also that way we can measure when one player lost.
        '''
        for k, v in target_ships.items():
            if coordinate in v:
                v.remove(coordinate)
                if len(v) == 0:
                    print("HIT & SUNK")
                else:
                    print("HIT")

    @staticmethod
    def player_status(target_ships):
        '''
            After a shot, checks if player has any unsunk boats and if he is
            still able to play, if all boats are sunk, game over.
        '''
        flatten_ships = [y for x in target_ships.values() for y in x]
        if len(flatten_ships) == 0:
            return True
        else:
            return False

    @staticmethod
    def machine_move():
        moves = list(range(1, 11))
        coordinate = tuple(random.choices(moves, k = 2))
        return coordinate


class Board:
    def __init__(self, columns, rows):
        self.rows = rows
        self.columns = columns
        self.board_array = self.board_array(self.rows, self.columns)

    def board_array(self, rows, columns):
        '''
            Creates the layout of the table
        '''
        board_array = []
        board_array.append(list(" "))
        board_array[0].append(" ".join(map(str, list(range(1, columns+1)))))
        #need to add +1 because one row in the board_array belongS to ascii characters
        for i in range(1, rows+1):
            board_array.append(list((f"{ i }", " ".join(" " * rows))))
        return board_array

    def render_board(self):
        '''
            Will render the state of a player's board
        '''
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

    def paint_shot(self, guess, shot):
        '''
            Marks X or M if hit or miss respectively
        '''
        if guess == True:
            icon = "X"
        elif guess == False:
            icon = "M"

        pos = list(self.board_array[shot[1]][1][::2])
        pos[shot[0]-1] = icon
        pos = " ".join(pos)
        self.board_array[shot[1]][1] = pos



class Player:
    def __init__(self):
        self.name = input("Player name: ").upper()
        self.player_ships = {}
        self.player_moves = []

    def define_ships(self, player_board, ships_settings):

        for s, l in ships_settings.items():
            temp_coordinates = []
            for n in range(l):
                while True:
                    print(f"Insert one coordinate at a time (eg: 3, 10) for each cell in : {s}")
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
                            print("Wrong input format", coordinate)
                            continue #will redirect to while loop
                    except (ValueError, ValueError):
                        print(f"Inser comma separated integers. Value is not valid")

                self.player_ships[s] = temp_coordinates
            player_board.set_pegs(self.player_ships[s])

    def perform_shot(self, player_tracking, target_board, target_ships, computer_coord = None):
        '''
            Calls for user input to ger shot coordinates and checks if
            the coordinates are inside target_ships
        '''
        while True:
            print(f"Insert one coordinate (eg: 1, 1) to perform a shot")
            try:

                if computer_coord == None:
                    coordinate = tuple(map(int, input().split(",")))
                else:
                    coordinate = computer_coord
                    if coordinate in self.player_moves: #to avoid infinite loop when a random choice generates same coordinates
                        print(f"DUPLICATE RANDOM CHOICE!!!!!!!!!!! {coordinate}")
                        coordinate = Game.machine_move()

                if Game.check_input(coordinate):
                    #checks if shot was executed in previous moves
                    if coordinate not in self.player_moves:
                        self.player_moves.append(coordinate)
                        ships = list(target_ships.values())
                        flatten_ships = [y for x in ships for y in x]
                        if coordinate in flatten_ships: #hit
                            guess = True
                            Game.delete_boat_pos(coordinate, target_ships)
                            #player_tracking.paint_shot(guess, flatten_ships, coordinate)
                            player_tracking.paint_shot(guess, coordinate)
                            #target_board.paint_shot(guess, flatten_ships, coordinate)
                            target_board.paint_shot(guess, coordinate)
                            break
                        else:
                            print("MISS")
                            guess = False
                            #player_tracking.paint_shot(guess, flatten_ships, coordinate)
                            player_tracking.paint_shot(guess, coordinate)
                            #MAYBE SHOULD ALSO MARK A MISS ON PLAYER2 BOARD
                            break
                    else:
                        print("COORDINATE ALREADY USED!")


            except (ValueError, ValueError):
                print(f"Inser comma separated integers. Value is not valid")


    def auto_boat_input(self, ships, player_board):
        '''
            Method to automatically input boats for testing and for
            inputting computers boats.
        '''
        self.player_ships = ships

        for s, l in ships.items():
            player_board.set_pegs(self.player_ships[s])
