class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        INF = 10 ** 20
        rows = len(word1)
        cols = len(word2)

        if not word1 or not word2: return max(rows, cols)

        dp = [[INF] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows + 1): dp[i][0] = i
        for j in range(cols + 1): dp[0][j] = j

        for i in range(rows):
            for j in range(cols):
                d = (1 if word1[i] != word2[j] else 0)
                dp[i + 1][j + 1] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i][j] + d)
        
        return dp[rows][cols]