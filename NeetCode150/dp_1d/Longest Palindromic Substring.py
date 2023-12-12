class Solution:
    def longestPalindrome(self, s):
        ans = s[-1]
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if (j - i == 1) or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if len(ans) < len(s[i:j + 1]):
                            ans = s[i:j + 1]
        
        return ans