class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 0
        max_profit = 0

        for i in range(len(prices)):

            if i == 0:
                min_price = prices[i]
                continue

            if min_price > prices[i]:
                min_price = prices[i]

            curr_profit = prices[i] - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
        
        return max_profit