class Solution:
    def isMatch(self, s, p):
        rows = len(s)
        cols = len(p)
        dp = [[False] * (cols + 1) for _ in range (rows + 1)]
        dp[0][0] = True

        for j in range(cols):
            if j - 1 >= 0 and p[j] == '*':
                dp[0][j + 1] |= dp[0][j - 1]
        
        for i in range(rows):
            for j in range(cols):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] |= dp[i][j]
                if j - 1 >= 0 and p[j] == '*':
                    dp[i + 1][j + 1] |= dp[i + 1][j - 1]
                    if s[i] == p[j - 1] or p[j - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i][j + 1]

        return dp[rows][cols]