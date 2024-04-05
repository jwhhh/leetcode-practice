from p0704 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append(([-1,0,3,5,9,12], 9))
solutions.append(4)

examples.append(([-1,0,3,5,9,12], 2))
solutions.append(-1)

examples.append(([5], 5))
solutions.append(0)


class TestCountAlternatingSubarrays(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.search(*example), solution)


if __name__ == '__main__':
    unittest.main()
