class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        hq = [(-nums[i], i) for i in range(k)]
        heapify(hq)
        ans = [-hq[0][0]]

        for i in range(k, len(nums)):
            while hq[0][1] <= i - k:
                heappop(hq)
            heappush(hq, (-nums[i], i))
            ans.append(-hq[0][0])
        
        return ans