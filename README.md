<h3 align="center">BATTLESHIP</h3>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)


## About the project
A small Battleship game project as a way to introduce myself into the object oriented programming.

### Prerequisites

To be able to run it you will need...(you probably guessed it):
* Python 3.6
Mac/Linux/Windows
```sh
python --version
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/YarosThk/battleship
```
### Code set up before running

In run.py you can predefine player_ships and player2_ships and pass them to the auto_boat_input()
which will automatically creat ship positions for each player. To do that follow instructions on lines 40-44.
However I suggest leaving the player2 (computer class) with auto_boat_input so it takes the already predefined ships,
because so far I have not come up with the code to randomly generate boat coordinates that respect the game rules.
For the meantime I think I will create a file which will contain different variations of boats, and with some random 
function it will generate a player2_ships (this is not implemented yet).



### Usage

1. Execute run.py 
2. Following that you will have to input a player1 and player 2 names and ship position one by one. 
    Coordinates are as follows 1, 1 = x (horizontal), y (vertical).
3. Once all ships are set, each player will take a turn to write a shot : 1, 1 = x (horizontal), y (vertical). Output : HIT, HIT & SUNK, MISS.
4. When one of the players gets all his/hers ships sunk, the game will be over.

## License

Distributed under the MIT License. See `LICENSE` for more information.
