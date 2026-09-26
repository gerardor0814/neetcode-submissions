class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retval = []

        for i in range(len(nums) - 2):
            curr = nums[i]
            if curr > 0:
                break

            if i > 0 and curr == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if curr + nums[left] + nums[right] > 0:
                    right -= 1
                elif curr + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    retval.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return retval