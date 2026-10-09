class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        retval = maxK

        while minK < maxK:
            totaltime = 0
            mid = int((minK + maxK)/2)
            for pile in piles:
                totaltime += math.ceil(pile/mid)
            if totaltime <= h:
                maxK = mid
                retval = maxK
            else:
                minK = mid + 1
        return retval
