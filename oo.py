import random
# Object Oriented Programming is a method of structuring a 
# program by bundling related properties
# and behaviors into individual objects, so you can handle lots 
# of stuff at once

#this is like a factory that constructs objects
# with the given materials
class Player:
    def __init__(self, name):
        self.name = name
        self.jersey_number = random.randint(1, 100)

    def __str__(self):
        return f"{self.name}: #{self.jersey_number}"
    
    def take_turn(self, gamepiece):
        gamepiece.position = input(f"Where would you like to put your {gamepiece.letter}? ")

class GamePieces:
    def __init__(self, letter, player, position=None):
        self.letter = letter
        self.player = player
        self.position = position

class Game:
    pass

# create an instance of a class
player1 = Player("Timothée")
player2 = Player("Oprah")
print(f'{player1.name}: #{player1.jersey_number} is playing against {player2.name}: #{player2.jersey_number}')
# create an X
first_x = GamePieces(letter="X", player=player1)
# put the x on the board
player1.take_turn(first_x)
print(f'{first_x.player} placed {first_x.letter} at position {first_x.position}')