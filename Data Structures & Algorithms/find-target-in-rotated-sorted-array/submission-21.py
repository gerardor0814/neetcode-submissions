class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return 0

        while l < r:
            mid = int((l + r) / 2)
            if nums[mid] > nums[r]:
                if target <= nums[r] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            elif nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid

        if nums[l] == target:
            return l
        else:
            return -1