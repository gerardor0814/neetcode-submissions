class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}

        for s in strs:
            srted = "".join(sorted(s))
            if srted in final:
                final[srted] = final[srted] + [s]
            else:
                final[srted] = [s]
        retval  = []
        for key, value in final.items():
            retval.append(value)

        return retval