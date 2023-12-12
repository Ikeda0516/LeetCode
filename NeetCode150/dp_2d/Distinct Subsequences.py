class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows = len(s)
        cols = len(t)
        t += '@'
        dp=[[0] * (cols + 1) for i in range(rows + 1)]
        dp[0][0] = 1
        
        for i in range(rows):
            for j in range(cols + 1):
                dp[i + 1][j] += dp[i][j]
                if s[i] == t[j]:
                    dp[i + 1][j + 1] += dp[i][j]

        return dp[rows][cols]