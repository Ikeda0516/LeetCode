class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for w in wordDict:
                if i - len(w) >= 0 and s[i - len(w):i] == w:
                    dp[i] |= dp[i - len(w)]
        
        return dp[n]