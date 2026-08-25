class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        front = 0
        back = len(heights) - 1
        while True:
            if front>back:
                break
            vol = min(heights[front], heights[back]) * (back-front)
            if vol>max_vol:
                max_vol = vol
            if heights[front]<=heights[back]:
                front+=1
            else:
                back -=1
        return max_vol