from p3100 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append([13, 6])
solutions.append(15)

examples.append([10, 3])
solutions.append(13)


class TestMaximumBottlesDrunk(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.maxBottlesDrunk(example[0], example[1]), solution)
        

if __name__ == '__main__':
    unittest.main()
