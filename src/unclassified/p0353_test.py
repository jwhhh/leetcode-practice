from p0353 import SnakeGame

import unittest

"""
Design a Snake game that is played on a device with screen size height x width.
Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of 
a piece of food that the snake can eat. When a snake eats a piece of food, its length 
and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food 
will not appear until the snake eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear 
on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies 
a space that its body occupies after moving (i.e. a snake of length 4 cannot run into 
itself).

Implement the SnakeGame class:

    SnakeGame(int width, int height, int[][] food) 
        Initializes the object with a screen of size height x width and the positions 
        of the food.
    int move(String direction) 
        Returns the score of the game after applying one direction move by the snake. 
        If the game is over, return -1.
"""

inputs = []
outputs = []


inputs.append(([
    "SnakeGame", "move", "move", "move", "move", "move", "move"], 
    [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
))
outputs.append([None, 0, 0, 1, 1, 2, -1])

inputs.append((
    ["SnakeGame","move","move","move","move","move","move","move","move","move","move","move","move"],
    [[3,3,[[2,0],[0,0],[0,2],[2,2]]],["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["D"]]
))
outputs.append([None,0,1,1,1,1,2,2,2,2,3,3,3])


class TestStringMethods(unittest.TestCase):
    def test_all(self):
        for i in range(len(inputs)):
            self._test_one(inputs[i], outputs[i])

    def _test_one(self, input_one, output_one):
        game = SnakeGame(*input_one[1][0])
        for i in range(1,len(output_one)):
            move = input_one[1][i][0]
            self.assertEqual(game.move(move), output_one[i], f"Wrong answer in move {i-1}: {move}")


if __name__ == '__main__':
    unittest.main()