from typing import List

class pySolution(object):
    def maxProfit(self, prices: List[int]) -> int:
        # 💰 Our treasure chest — stores the best profit we can make so far
        maxprofit: int = 0
        
        # 📅 Total number of trading days available
        n: int = len(prices)

        # 🛒 Step 1: Pick a day to BUY the stock
        for currentDay in range(n - 1):
            # 💵 Price of the stock on the buying day
            buyingPrice: int = prices[currentDay]
            
            # 🔭 Step 2: Look into the future to find the best day to SELL
            for futureDay in range(currentDay + 1, n):
                # 💸 Price of the stock on the selling day
                sellingPrice: int = prices[futureDay]
                
                # 📊 Calculate profit if we buy today and sell on this future day
                profit: int = sellingPrice - buyingPrice
                
                # 🧠 Decision time:
                #    Keep the old profit OR replace it with a better one
                maxprofit = max(maxprofit, profit)

        # 🚀 Return the maximum profit earned
        #    (If no profitable deal exists, this naturally stays 0)
        return maxprofit