class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l: return 0

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m): dp[i + 1][0] = (dp[i][0] and s1[i] == s3[i])
        for j in range(n): dp[0][j + 1] = (dp[0][j] and s2[j] == s3[j])

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = (dp[i][j + 1] and s1[i] == s3[i + j + 1]) or (dp[i + 1][j] and s2[j] == s3[i + j + 1])
        
        return dp[m][n]