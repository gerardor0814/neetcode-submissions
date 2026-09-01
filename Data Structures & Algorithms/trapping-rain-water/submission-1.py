class Solution:
    def trap(self, height: List[int]) -> int:
        sol = 0

        if len(height) == 0:
            return sol
        
        leftMax = [0 for i in range(len(height))]
        rightMax = [0 for i in range(len(height))]

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        for i in range(len(height)):
            sol += min(leftMax[i], rightMax[i]) - height[i]

        return sol
        