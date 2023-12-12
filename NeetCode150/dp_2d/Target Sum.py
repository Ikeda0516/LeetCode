class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if not (-total <= target <= total):
            return 0

        m = len(nums)
        n = total * 2 + 1
        dp = [[0] * n for i in range(m)]
        dp[0][total + nums[0]] += 1
        dp[0][total - nums[0]] += 1
        
        for i in range(1, m):
            for j in range(n):
                if j - nums[i] >= 0 and dp[i - 1][j - nums[i]] > 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]
                if j + nums[i] <= total * 2 and dp[i - 1][j + nums[i]] > 0:
                    dp[i][j] += dp[i - 1][j + nums[i]]
        
        return dp[m - 1][total + target]