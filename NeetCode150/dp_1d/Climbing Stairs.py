class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(n - 1):
            dp[i + 2] = dp[i + 1] + dp[i]
        
        return dp[n]