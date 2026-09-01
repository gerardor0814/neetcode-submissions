class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sol = dict()
        comp = dict()

        for char in s:
            if char in sol:
                sol[char] +=1
            else:
                sol[char] = 1
        
        for char in t:
            if char in comp:
                comp[char] +=1
            else:
                comp[char] = 1
        
        return sol == (comp)
