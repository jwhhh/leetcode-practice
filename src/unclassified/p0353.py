from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food

        self.snake_pos = [(0,0)]
        self.food_i = 0
        self.current_food = self.food[self.food_i]
        self.score = 0

    def move(self, direction: str) -> int:
        snake_head = self.snake_pos[0]

        if direction == "U":
            new_snake_pos = (snake_head[0] - 1, snake_head[1])
        elif direction == "D":
            new_snake_pos = (snake_head[0] + 1, snake_head[1])
        elif direction == "L":
            new_snake_pos = (snake_head[0], snake_head[1] - 1)
        elif direction == "R":
            new_snake_pos = (snake_head[0], snake_head[1] + 1)
        else:
            raise ValueError(f"Invalid direction code {direction}")

        self.snake_head = new_snake_pos

        if self._check_out_of_bound():
            return -1

        self._check_food()

        if self._check_eat_itself():
            return -1

        self.snake_pos.insert(0, new_snake_pos)

        self._consume_food()

        return self.score

    def _check_out_of_bound(self):
        return not (0 <= self.snake_head[0] < self.height and 0 <= self.snake_head[1] < self.width)

    def _check_eat_itself(self):
        return self.snake_head in (self.snake_pos if self._has_food else self.snake_pos[:-1])

    def _check_food(self):
        self._has_food = self.current_food and tuple(self.current_food) == self.snake_head

    def _consume_food(self):
        if self._has_food:
            self.score += 1
            self.food_i += 1
            self.current_food = self.food[self.food_i] if self.food_i < len(self.food) else None
        else:
            self.snake_pos.pop()


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)