# Greedy Approach
The key idea 💡 is:
- Always keep track of the **minimum stock price seen so far**
- For each day, calculate the profit if the stock is sold on that day
- Update the maximum profit accordingly

This avoids checking all possible buy–sell pairs and gives the optimal result in one pass.

### 🧩 Algorithm Steps
1. Initialize:
    - `buyingPrice` = price on Day 0
    - `maxProfit` = 0
2. Iterate from Day 1 to the last day:
    - Calculate `currentPrice - buyingPrice`
    - Update `maxProfit` if the profit is higher
    - Update `buyingPrice` if a lower price is found
3. Return `maxProfit`

### ⏱️ Complexity Analysis
- **Time Complexity**:- `O(n)`
- **Space Complexity**:- `O(1)`
---