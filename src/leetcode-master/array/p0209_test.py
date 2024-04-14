from p0209 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append([7, [2,3,1,2,4,3]])
solutions.append(2)

examples.append([4, [1,4,4]])
solutions.append(1)

examples.append([11, [1,1,1,1,1,1,1,1]])
solutions.append(0)


class Test(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])
    
    def _test_one(self, example, solution):
        self.assertEqual(sol.minSubArrayLen(*example), solution)
        

if __name__ == "__main__":
    unittest.main()
