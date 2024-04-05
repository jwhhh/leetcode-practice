from p0977 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append([-4,-1,0,3,10])
solutions.append([0,1,9,16,100])

examples.append([-7,-3,2,3,11])
solutions.append([4,9,9,49,121])


class Test(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.sortedSquares(example), solution)


if __name__ == '__main__':
    unittest.main()
