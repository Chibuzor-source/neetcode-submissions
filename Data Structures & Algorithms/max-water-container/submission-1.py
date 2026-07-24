class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_Area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            min_height = min(heights[l], heights[r])
            width = r - l
            cur_Area = min_height * width
            max_Area = max(cur_Area, max_Area)
            if heights[l] == min_height:
                l += 1
            else:
                r -= 1
        return max_Area