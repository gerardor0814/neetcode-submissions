class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1 = Counter(s1)

        l = 0

        for i in range(len(s1) - 1, len(s2)):
            freq2 = Counter(s2[l:i+1])
            if freq1 == freq2:
                return True
            l += 1

        return False