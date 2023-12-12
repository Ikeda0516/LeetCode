class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                val, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((temperatures[i], i))
        
        return ans