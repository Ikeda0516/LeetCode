class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 1 << 33
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        
        return dp[amount] if dp[amount] != INF else -1