class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = dict()

        for i in range (0, len(nums)):
            sol[nums[i]] = i

        for i in range (0, len(nums)):
            if target - nums[i] in sol and sol[target - nums[i]] != i:
                return [i, sol[target-nums[i]]]

        return []