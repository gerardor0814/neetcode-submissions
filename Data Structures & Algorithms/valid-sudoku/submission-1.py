class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareHashMap = defaultdict(set)
        colHashMap = defaultdict(set)

        for i in range(9):
            rowHash = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowHash or board[i][j]in colHashMap[j] or board[i][j] in squareHashMap[(i//3) * 3 + (j//3)]:
                    return False
                else:
                    rowHash.add(board[i][j])
                    colHashMap[j].add(board[i][j])
                    squareHashMap[(i//3) * 3 + (j//3)].add(board[i][j])
        return True