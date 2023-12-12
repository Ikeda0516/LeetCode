class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = [-10 ** 5] + nums
        i = bisect_left(nums, target)
        if 0 < i < len(nums) and nums[i] == target:
            return i - 1
        else:
            return -1