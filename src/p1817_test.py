from p1817 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append(([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))
solutions.append([0,2,0,0,0])

examples.append(([[1,1],[2,2],[2,3]], 4))
solutions.append([1,1,0,0])


class TestStringMethods(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.findingUsersActiveMinutes(example[0], example[1]), solution)


if __name__ == '__main__':
    unittest.main()