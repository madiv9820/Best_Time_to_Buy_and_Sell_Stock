#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 💰 Stores the maximum profit we can make
        int maxprofit = 0;

        // 🛒 Buying price starts with Day 0 price
        int buyingPrice = prices[0];

        // 📅 Traverse prices starting from Day 1
        for (int currentDay = 1; currentDay < prices.size(); ++currentDay) {
            // 💵 Current day's stock price
            int currentPrice = prices[currentDay];

            // 📊 Profit if we sell today at the best buying price so far
            int profit = currentPrice - buyingPrice;

            // 🧠 Update maximum profit if today's profit is better
            maxprofit = max(maxprofit, profit);

            // 🔄 Update buying price if we find a cheaper price
            //    (Always aim to buy at the lowest possible price)
            buyingPrice = (currentPrice < buyingPrice) ? currentPrice : buyingPrice;
        }

        // 🚀 Return the maximum profit
        //    (Returns 0 if no profitable transaction is possible)
        return maxprofit;
    }
};