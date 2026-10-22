class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = set()
        subsets.add(())
        for num in nums:
            for sub in subsets.copy():
                subsets.add(sub + (num, ))

        return [list(item) for item in subsets]