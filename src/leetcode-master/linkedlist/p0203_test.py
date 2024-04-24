from p0203 import Solution, ListNode

import unittest


sol = Solution()

examples = []
solutions = []

head1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
examples.append((head1, 6))
solutions.append([1,2,3,4,5])

examples.append((None, 1))
solutions.append([])

head3 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
examples.append((head3, 7))
solutions.append([])


class Test(unittest.TestCase):
    def test_all(self):
        for i in range(len(examples)):
            self._test_one(examples[i], solutions[i])
    
    def _test_one(self, example, solution):
        self.assertEqual(ListNode.to_list(sol.removeElements(*example)), solution)


if __name__ == "__main__":
    unittest.main()
