class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            ans += 1
        
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if (s[i] == s[j]) and (j - i == 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j]:
                    ans += 1
        
        return ans