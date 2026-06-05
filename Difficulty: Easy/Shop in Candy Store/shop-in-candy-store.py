class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        n = len(prices)
        
        i = 0
        end = n - 1
        minCost = 0
        
        while i <= end:
            minCost += prices[i]
            
            i += 1
            
            end -= k
        
        i = n - 1
        end = 0
        maxCost = 0
        while i >= end:
            maxCost += prices[i]
            
            i -= 1
            end += k
        
        return [minCost, maxCost]