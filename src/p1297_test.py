from p1297 import Solution

import unittest

sol = Solution()

inputs = []
outputs = []

inputs.append({"s": "aababcaab", "maxLetters": 2, "minSize": 3, "maxSize": 4})
outputs.append(2)

inputs.append({"s": "aaaa", "maxLetters": 1, "minSize": 3, "maxSize": 3})
outputs.append(2)

inputs.append({"s": "aabcabcab", "maxLetters": 2, "minSize": 2, "maxSize": 3})
outputs.append(3)

inputs.append({"s": "abcde", "maxLetters": 2, "minSize": 3, "maxSize": 3})
outputs.append(0)


class TestMaxFreq(unittest.TestCase):
    def test_all(self):
        for i in range(len(inputs)):
            self._test_one(inputs[i], outputs[i])

    def _test_one(self, input_one, output_one):
        self.assertEqual(
            sol.maxFreq(**input_one), 
            output_one, 
            f"test case of input {input_one} and expected output {output_one}"
        )


if __name__ == '__main__':
    unittest.main()

