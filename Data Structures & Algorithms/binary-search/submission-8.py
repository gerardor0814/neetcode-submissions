class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recur(nums, target, l, r):
            curr = int((r + l) / 2)
            if l > r:
                return -1
            elif target == nums[curr]:
                return curr
            elif target > nums[curr]:
                return recur(nums, target, curr + 1, r)
            else:
                return recur(nums, target, l, curr - 1)

        return recur(nums, target, 0, len(nums) - 1)