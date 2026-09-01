from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for num in freq:
            sol[freq[num]].append(num)
        
        retVal = []
        for i in range(len(sol) - 1, 0, -1):
            for num in sol[i]:
                retVal.append(num)
                if len(retVal) == k:
                    return retVal