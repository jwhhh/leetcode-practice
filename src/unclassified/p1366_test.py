from p1366 import Solution

import unittest


sol = Solution()

examples = []
solutions = []

examples.append(["ABC","ACB","ABC","ACB","ACB"])
solutions.append("ACB")

examples.append(["WXYZ","XYZW"])
solutions.append("XWYZ")

examples.append(["ZMNAGUEDSJYLBOPHRQICWFXTVK"])
solutions.append("ZMNAGUEDSJYLBOPHRQICWFXTVK")

examples.append(["BCA","CAB","CBA","ABC","ACB","BAC"])
solutions.append("ABC")

examples.append(["M","M","M","M"])
solutions.append("M")


class TestStringMethods(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])

    def _test_one(self, example, solution):
        self.assertEqual(sol.rankTeams(example), solution)


if __name__ == '__main__':
    unittest.main()
