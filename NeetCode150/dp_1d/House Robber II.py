class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: 
            return nums[0]

        def subRob(i, j):
            N = len(nums[i:j])
            dp = [[None, None] for _ in range(N)]

            dp[0][0] = 0
            dp[0][1] = nums[i]
            for k in range(N - 1):
                dp[k + 1][0] = max(dp[k][0], dp[k][1])
                dp[k + 1][1] = dp[k][0] + nums[k + 1 + i]
        
            return max(dp[N - 1][0], dp[N - 1][1])

        return max(subRob(0, n - 1), subRob(1, n))