from typing import List

class pySolution(object):
    def maxProfit(self, prices: List[int]) -> int:
        # 💰 Stores the maximum profit we can make
        maxprofit: int = 0
        
        # 🛒 Buying price starts as the price on Day 0
        buyingPrice: int = prices[0]

        # 📅 Iterate through prices starting from Day 1
        for currentPrice in prices[1:]:
            # 📊 Profit if we sell today using the lowest buying price so far
            profit: int = currentPrice - buyingPrice
            
            # 🧠 Update maximum profit if today's profit is better
            maxprofit = max(maxprofit, profit)
            
            # 🔄 Update buying price if we find a cheaper stock price
            #    (Always buy at the lowest possible price)
            buyingPrice = currentPrice if currentPrice < buyingPrice else buyingPrice
        
        # 🚀 Return the maximum profit
        #    (Returns 0 if no profitable transaction exists)
        return maxprofit