from p0059 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append(3)
solutions.append([[1,2,3],[8,9,4],[7,6,5]])

# 0, 3, 0, 3
# 1, 3, 0, 3
# 1, 3, 0, 2
# 1, 2, 0, 2
# 

examples.append(1)
solutions.append([[1]])


class Test(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])
    
    def _test_one(self, example, solution):
        self.assertEqual(sol.generateMatrix(example), solution)
        

if __name__ == "__main__":
    unittest.main()
