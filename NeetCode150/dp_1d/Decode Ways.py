class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if i - 1 >= 0 and 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i + 1] += dp[i - 1]
        
        return dp[n]