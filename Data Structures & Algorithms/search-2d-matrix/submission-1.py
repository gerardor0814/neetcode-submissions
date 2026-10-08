class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def recurMatrix(matrix, target, top, bot):
            row = int((top + bot) / 2)

            if top > bot:
                return False
            if target > matrix[row][-1]:
                return recurMatrix(matrix, target, row + 1, bot)
            elif target < matrix[row][0]:
                return recurMatrix(matrix, target, top, row - 1)
            else:
                return recurRow(matrix[row], target, 0, len(matrix[row]) - 1)
        
        def recurRow(nums, target, l, r):
            curr = int((r + l) / 2)
            if l > r:
                return False
            elif target == nums[curr]:
                return True
            elif target > nums[curr]:
                return recurRow(nums, target, curr + 1, r)
            else:
                return recurRow(nums, target, l, curr - 1)

        return recurMatrix(matrix, target, 0, len(matrix) - 1)

        