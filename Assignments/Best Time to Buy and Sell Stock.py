from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(day: int, stock: int, transaction: int) -> int:
            if day == n or transaction >= 1:
                return 0
            if (day, stock, transaction) in memo:
                return memo[(day, stock, transaction)]
            if stock == 0:
                ## buy
                buy = -prices[day] + dp(day + 1, 1, transaction)
                keep = 0 + dp(day + 1, 0, transaction)
                profit = max(buy, keep)
                memo[(day, stock, transaction)] = profit
                return profit
            else:
                ## sell
                sell = prices[day] + dp(day + 1, 0, transaction + 1)
                keep = 0 + dp(day + 1, 1, transaction)
                profit = max(sell, keep)
                memo[(day, stock, transaction)] = profit
                return profit

        return dp(0, 0, 0)
