class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 0, 10 ** 9 + 1

        while right - left > 1:
            mid = (left + right) // 2
            if sum((pile + mid - 1) // mid for pile in piles) <= h:
                right = mid
            else:
                left = mid
        return right