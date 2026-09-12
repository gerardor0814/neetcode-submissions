class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countlist = [[] for i in range(len(nums) + 1)]
        countdict = defaultdict(int)

        for num in nums:
            countdict[num] += 1
        
        for num, count in countdict.items():
            countlist[count].append(num)
        
        retval = []
        i = len(nums) - 1
        while True:
            for num in countlist[i]:
                retval.append(num)
                if len(retval) == k:
                    return retval
            i -= 1

