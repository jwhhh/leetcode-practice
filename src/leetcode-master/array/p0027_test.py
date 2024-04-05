from p0027 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append(([3,2,2,3], 3))
solutions.append(([2,2], 2))

examples.append(([0,1,2,2,3,0,4,2], 2))
solutions.append(([0,1,4,0,3], 5))


class Test(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        nums, val = example
        expected_nums, expected_k = solution
        resulted_k = sol.removeElement(nums, val)
        expected_sorted = sorted(expected_nums[:expected_k])
        resulted_sorted = sorted(nums[:resulted_k])
        self.assertEqual(expected_sorted, resulted_sorted)


if __name__ == '__main__':
    unittest.main()
