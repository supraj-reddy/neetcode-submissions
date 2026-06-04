class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, best = 0, 0
        seen = {}
        for i, last in enumerate(s):
            if last in seen and seen[last] >= start:
                start = seen[last] + 1
            seen[last] = i
            best = max(best, i - start + 1)
        return best