class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retval = [[]]
        start = end = 0
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                start = end
            else:
                start = 0
            end = len(retval)
            for j in range(start, end):
                new = retval[j].copy()
                new.append(nums[i])
                retval.append(new)
        
        return retval