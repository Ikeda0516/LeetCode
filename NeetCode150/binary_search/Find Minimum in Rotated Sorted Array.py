class Solution:
    def findMin(self, nums: List[int]) -> int:
        ng = -1
        ok = len(nums)
        
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if nums[mid] <= nums[-1]:
                ok = mid
            else:
                ng = mid
        return nums[ok]