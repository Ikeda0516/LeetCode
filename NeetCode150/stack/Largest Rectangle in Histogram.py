class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
        stack = []
        ans = 0

        for bar in bars + [-1]:
            step = 0
            while stack and stack[-1][1] >= bar:
                w, h = stack.pop()
                step += w
                ans = max(ans, step * h)
            stack.append((step + 1, bar))

        return ans