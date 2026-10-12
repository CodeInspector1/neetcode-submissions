class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        f = 0
        s = len(heights) - 1

        while f < s:
            w = s - f
            
            h = min(heights[f], heights[s])

            curr = w * h

            if curr > result:
                result = curr
            
            if heights[f] < heights[s]:
                f += 1
            else:
                s -= 1
        
        return result
            