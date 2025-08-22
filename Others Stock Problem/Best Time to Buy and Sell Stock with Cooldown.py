from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def dp(day: int, stock: int) -> int:
            if day >= n:
                return 0
            if (day, stock) in memo:
                return memo[(day, stock)]
            if stock == 0:
                ## buy
                buy = -prices[day] + dp(day + 1, 1)
                keep = 0 + dp(day + 1, 0)
                profit = max(buy, keep)
                memo[(day, stock)] = profit
                return profit
            else:
                ## sell
                sell = prices[day] + dp(day + 2, 0)
                keep = 0 + dp(day + 1, 1)
                profit = max(sell, keep)
                memo[(day, stock)] = profit
                return profit

        return dp(0, 0)
