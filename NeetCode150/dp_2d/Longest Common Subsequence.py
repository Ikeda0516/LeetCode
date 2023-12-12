class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                 d = (1 if s1[i] == s2[j] else 0)
                 dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + d)
        
        return dp[m][n]