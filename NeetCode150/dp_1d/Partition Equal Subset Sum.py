class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(target + 1):
                dp[i + 1][j] |= dp[i][j]
                if j - nums[i] >= 0:
                    dp[i + 1][j] |= dp[i][j - nums[i]]
        
        return dp[n][target]