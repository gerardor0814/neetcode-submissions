class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        retval = 0
        left = 0
        right = 0
        for c in s:
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            right += 1
            retval = max(retval, right - left)
        return retval