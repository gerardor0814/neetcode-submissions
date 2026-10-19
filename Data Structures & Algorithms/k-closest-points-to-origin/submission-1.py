class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidian = []
        retval = []
        for i in range(len(points)):
            euclidian.append((math.sqrt((points[i][0] ** 2) + points[i][1] ** 2), i))

        heapq.heapify(euclidian)

        for _ in range(k):
            smallest = heapq.heappop(euclidian)
            retval.append(points[smallest[1]])

        return retval