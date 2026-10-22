class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [1]
        retval = []
        def dfs(par, op, cl):
            if op < n:
                dfs(par + '(', op + 1, cl)
            if cl < op:
                dfs(par + ')', op, cl + 1)

            if op == n and cl == n:
                retval.append(par)
                return
            
        dfs("", 0, 0)
        return retval