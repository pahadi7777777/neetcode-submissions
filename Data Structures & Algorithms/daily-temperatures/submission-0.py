class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t > stack [-1][0]:
                stackT,stackIND = stack.pop()
                result[stackIND] = (i-stackIND)

            stack.append([t,i])
        return result