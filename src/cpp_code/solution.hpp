#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 📅 Total number of days in the stock market
        int n = prices.size();
        
        // 💰 Stores the maximum profit we can achieve
        int maxprofit = 0;

        // 🛒 Step 1: Choose a day to BUY the stock
        for (int currentDay = 0; currentDay < n - 1; ++currentDay) {
            // 💵 Price of the stock on the buying day
            int buyingPrice = prices[currentDay];

            // 🔭 Step 2: Look into the future for a day to SELL
            for (int futureDay = currentDay + 1; futureDay < n; ++futureDay) {
                // 💸 Price of the stock on the selling day
                int sellingPrice = prices[futureDay];

                // 📊 Profit if we buy on currentDay and sell on futureDay
                int profit = sellingPrice - buyingPrice;

                // 🧠 Keep the best profit seen so far
                maxprofit = max(maxprofit, profit);
            }
        }

        // 🚀 Return the maximum profit
        //    (0 if no profitable transaction is possible)
        return maxprofit;
    }
};