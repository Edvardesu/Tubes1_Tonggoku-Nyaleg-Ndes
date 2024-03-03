from typing import Tuple
from game.logic.base import BaseLogic
from game.models import Board, GameObject



class MyBot(BaseLogic):
    def __init__(self):
        # Initializes attributes necessary
        self.my_attribute = 0
    
    def next_move(self, board_bot: GameObject, board: Board):
        # Calculate next move
        delta_x = 1
        delta_y = 1
        return delta_x, delta_y


