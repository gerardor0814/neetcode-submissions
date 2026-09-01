class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        sol = []

        for i in range(len(sortedNums)):
            l = i + 1
            r = len(sortedNums) - 1

            if sortedNums[i] > 0:
                break

            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue

            while l < r:
                if sortedNums[l] + sortedNums[r] + sortedNums[i] == 0:
                    sol.append([sortedNums[i], sortedNums[r], sortedNums[l]])
                    l += 1
                    r -= 1
                    while sortedNums[l] == sortedNums[l-1] and l < r:
                        l += 1
                elif sortedNums[l] + sortedNums[r] > -sortedNums[i]:
                    r -= 1
                else:
                    l += 1
        return sol


