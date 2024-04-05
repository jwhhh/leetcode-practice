class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        return self.max_bottles_drunk(numBottles, 0, numExchange)
        
    def max_bottles_drunk(
        self, 
        num_full_bottles: int, 
        num_empty_bottles:int , 
        num_exchange: int
    ) -> int:
        max_num_bottles_drunk = 0
        if num_full_bottles:
            drink_n_bottles = num_full_bottles
            new_num_full_bottles = num_full_bottles - drink_n_bottles
            new_num_empty_bottles = num_empty_bottles + drink_n_bottles
            new_bottles_drunk = self.max_bottles_drunk(
                new_num_full_bottles, new_num_empty_bottles, num_exchange
            ) + drink_n_bottles
            if new_bottles_drunk > max_num_bottles_drunk:
                max_num_bottles_drunk = new_bottles_drunk
        if num_empty_bottles >= num_exchange:
            new_num_full_bottles = num_full_bottles + 1
            new_num_empty_bottles = num_empty_bottles - num_exchange
            new_num_exchange = num_exchange + 1
            new_bottles_drunk = self.max_bottles_drunk(
                new_num_full_bottles, new_num_empty_bottles, new_num_exchange
            )
            if new_bottles_drunk > max_num_bottles_drunk:
                max_num_bottles_drunk = new_bottles_drunk
        return max_num_bottles_drunk
    
    # Drink any number of full water bottles turning them into empty bottles.
    # Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
