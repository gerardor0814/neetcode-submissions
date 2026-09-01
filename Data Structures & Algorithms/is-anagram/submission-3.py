class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        count2 = dict()
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in t:
            if c in count2:
                count2[c] += 1
            else:
                count2[c] = 1

        return count == count2  