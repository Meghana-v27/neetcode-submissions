class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit,min_price=0,float('inf')
        for x in prices:
            if x<min_price:
                min_price=x
            profit=x-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit
