class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        now = n - 1

        for i in reversed(range(n - 1)):
            if i + nums[i] >= now:
                now = i
        
        return now == 0