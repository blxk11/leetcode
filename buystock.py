from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_prices = 0

        for i in prices:
            if i < min_prices:
                min_prices = i
            else:
                profit = i - min_prices
                if profit > max_prices:
                    max_prices = profit

        return max_prices  # ✅ outside the loop