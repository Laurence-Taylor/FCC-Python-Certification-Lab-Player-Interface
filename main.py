from abc import ABC, abstractmethod
import random

class Player(ABC):
    """Class Player"""
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        next_move = random.choice(self.moves)
        new_x = next_move[0] + self.position[0]
        new_y = next_move[1] + self.position[1]
        new_position = (new_x, new_y)
        self.position = new_position
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):

    def __init__(self):
        super().__init__()
        self.moves =[(1,0), (-1,0),(0,1),(0,-1)]

    def level_up(self):
        new_moves = [(1,1), (1,-1), (-1,1), (-1,-1)]
        self.moves += new_moves

if __name__ == "__main__":    
    player1 = Pawn()
    player1.make_move()
    print(player1.moves)
    player1.make_move()
    print(player1.position)
    print(player1.path)
    player1.make_move()
    print(player1.path)
    print(player1.position)
    player1.level_up()
    print(player1.moves)