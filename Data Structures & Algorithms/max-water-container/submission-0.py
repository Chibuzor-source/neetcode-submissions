class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_Area = 0
        for i in range(len(heights)):
            r = len(heights) - 1
            while i < r:
                min_height = min(heights[i], heights[r])
                width = r - i
                cur_Area = min_height * width
                max_Area = max(cur_Area, max_Area)
                r -= 1

        return max_Area