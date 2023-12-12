class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        Lmin = [0] * N
        Lmin[0] = prices[0]
        for i in range(N - 1):
            Lmin[i + 1] = min(Lmin[i], prices[i + 1])

        ans = 0
        for i in range(N - 1):
            ans = max(ans, prices[i + 1] - Lmin[i])
        
        return ans