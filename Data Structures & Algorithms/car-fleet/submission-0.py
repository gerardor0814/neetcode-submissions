class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [[0, 0] for i in range(len(position))]
        stack = []
        for i in range(len(position)):
            combined[i][0] = position[i]
            combined[i][1] = speed[i]
        
        combined.sort(reverse = True)

        for item in combined:
            arrival = (target - item[0])/item[1]
            if not stack or arrival > stack[-1]:
                stack.append(arrival)
                    
        return len(stack)