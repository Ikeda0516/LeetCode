class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(n - 1):
            dp[i + 1] = max(nums[i + 1] + dp[i], nums[i + 1])
        
        return max(dp)