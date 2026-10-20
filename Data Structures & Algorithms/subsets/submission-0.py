class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retval = [[]]
        for num in nums:
            for val in retval[:]:
                new = val.copy()
                new.append(num)
                retval.append(new)
        return retval