class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    continue
                
                width = abs(i - j)
                length = min(heights[i], heights[j])
                max_area = max(max_area, width * length)

        return max_area