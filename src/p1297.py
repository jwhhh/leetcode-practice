from collections import deque

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        stats = dict()
        max_stats = 0
        len_s = len(s)
        if len_s < minSize: 
            return 0

        sub_chars = deque(list(s[:minSize]))
        for i in range(len_s-minSize+1):
            j = i + minSize   # the j-th is not included
            if i != 0:
                sub_chars.append(s[j-1])
                sub_chars.popleft()
            if len(set(sub_chars)) <= maxLetters:
                sub_string = ''.join(sub_chars)
                if sub_string not in stats:
                    stats[sub_string] = 0
                stats[sub_string] += 1
                if stats[sub_string] > max_stats:
                    max_stats = stats[sub_string]
        return max_stats
