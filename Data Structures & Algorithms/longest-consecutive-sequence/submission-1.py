class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        solSet = set(nums)
        maxi = 0
        for num in solSet:
            if num - 1 not in solSet:
                curr = num
                temp = 0
                while curr in solSet:
                    temp += 1
                    curr += 1
                if temp > maxi:
                    maxi = temp
        return maxi
        