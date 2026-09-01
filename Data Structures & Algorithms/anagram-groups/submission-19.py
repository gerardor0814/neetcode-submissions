class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = dict()
        solArr = []

        for i in range (0, len(strs)):
            sort = ''.join(sorted(strs[i]))
            if sort in sol:
                print(sol)
                sol[sort] = sol[sort] + [i]
            else:
                sol[sort] = [i]

        for val in sol:
            temp = []
            for ind in sol[val]:
                temp.append(strs[ind])
            solArr.append(temp)

        return solArr