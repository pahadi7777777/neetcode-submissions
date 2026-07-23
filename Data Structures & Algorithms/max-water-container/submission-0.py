class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        result = []

        while l < r:
            if heights[l] > heights[r]:
                mult = (r-l) * heights[r]
                r -= 1
            else:
                mult = (r-l) * heights[l]
                l += 1
            result.append(mult)
        return max(result)
