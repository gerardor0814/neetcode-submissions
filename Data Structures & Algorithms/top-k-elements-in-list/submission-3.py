class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        rank = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            rank[value].append(key)

        res = []
        for i in range(len(rank) - 1, 0, -1):
            for num in rank[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
        