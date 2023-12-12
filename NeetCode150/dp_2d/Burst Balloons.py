class Solution:
    def maxCoins(self, nums):
        if not nums:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for l in reversed(range(n)):
            for r in range(l, n):
                for i in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r])

        return dp[0][n - 1]