class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        sol = nums
        hasZero = False
        for num in nums:
            if num == 0:
                if hasZero:
                    total *= num
                hasZero = True
            else:
                total *= num
        for i in range(len(nums)):
            if total == 0:
                sol[i] = 0
            elif hasZero and sol[i] != 0:
                sol[i] = 0
            elif sol[i] == 0:
                sol[i] = total
            else:
                sol[i] = int(total/sol[i]) 

        return sol
        