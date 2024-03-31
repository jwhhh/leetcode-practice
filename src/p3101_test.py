from p3101 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append([0, 1, 1, 1])
solutions.append(5)

examples.append([1, 0, 1, 0])
solutions.append(10)


class TestCountAlternatingSubarrays(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.countAlternatingSubarrays(example), solution)


if __name__ == '__main__':
    unittest.main()
