class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        arr = []

        for i in range(n):
            dp[i] = bisect_left(arr, nums[i])
            if dp[i] >= len(arr):
                arr.append(nums[i])
            else:
                arr[dp[i]] = nums[i]
        
        return max(dp) + 1