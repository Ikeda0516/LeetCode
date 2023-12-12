class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        
        dpBuy = [-10 ** 9] * n
        dpSell = [0] * n

        for i in range(n):
            dpBuy[i] = max(dpBuy[i - 1], dpSell[i - 2] - prices[i])
            dpSell[i] = max(dpSell[i - 1], dpBuy[i - 1] + prices[i])
        
        return dpSell[-1]