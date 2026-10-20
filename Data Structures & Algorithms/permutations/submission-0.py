class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        retval = []

        def backtrack(perm, seen):
            if len(perm) == len(nums):
                retval.append(perm.copy())
            for i in range(len(nums)):
                if not seen[i]:
                    seen[i] = True
                    perm.append(nums[i])
                    backtrack(perm, seen)
                    perm.pop()
                    seen[i] = False
        
        backtrack([], [False] * len(nums))
        return retval