# Given a string s, return the maximum number of ocurrences of any substring under the following rules:

#     The number of unique characters in the substring must be less than or equal to maxLetters.
#     The substring size must be between minSize and maxSize inclusive.

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        stats = dict()
        max_stats = 0
        len_s = len(s)
        for i in range(len_s-minSize+1):
            for l in range(minSize, maxSize+1):
                j = i + l   # the j-th is not included
                if j > len_s: break
                substring = s[i:j]
                if len(set(list(substring))) <= maxLetters:
                    if substring not in stats:
                        stats[substring] = 0
                    stats[substring] += 1
                    if stats[substring] > max_stats:
                        max_stats = stats[substring]
        return max_stats
