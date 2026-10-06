class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        end = 0
        maxlen = 0
        while end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            maxlen = max(maxlen, end - start + 1)
            end += 1
        return maxlen