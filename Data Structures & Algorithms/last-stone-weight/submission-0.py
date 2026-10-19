class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if largest == second:
                continue
            else: 
                new = largest - second
                heapq.heappush(stones, -new)

        return -heapq.heappop(stones) if stones else 0