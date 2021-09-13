# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        if len(prices)==1:
            return 0
        if len(prices)==2:
            if prices[1]-prices[0]>0:
                return prices[1]-prices[0]
            else:
                0
        profit = prices[r]-prices[l]
        mp = 0
        while r<len(prices) :
            profit = prices[r]-prices[l]
            if profit<0:
                l+=1
            else:
                r+=1
            if profit>mp:
                mp = profit
        return mp
            