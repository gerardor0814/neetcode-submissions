class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recur(nums, target, add):
            curr = int(len(nums) / 2)
            if target == nums[curr]:
                return curr + add
            elif len(nums) == 1 and nums[0] != target:
                return -1
            elif target > nums[curr]:
                return recur(nums[curr: len(nums)], target, curr + add)
            else:
                return recur(nums[0: curr], target, add)
        return recur(nums, target, 0)