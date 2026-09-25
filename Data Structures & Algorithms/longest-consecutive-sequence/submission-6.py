class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            localMax = 1
            curr = num
            if num - 1 not in numsSet:
                while curr + 1 in numsSet:
                    print(curr)
                    localMax += 1
                    curr = curr + 1
            if localMax > longest:
                longest = localMax
        
        return longest