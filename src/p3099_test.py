from p3099 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append(18)
solutions.append(9)

examples.append(23)
solutions.append(-1)


class TestHarshadNumber(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.sumOfTheDigitsOfHarshadNumber(example), solution)
        

if __name__ == '__main__':
    unittest.main()
