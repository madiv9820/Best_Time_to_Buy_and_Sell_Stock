#  Brute Force Approach

The idea💡 is simple and intuitive:
1. 📅 Pick each day as a **buying day**
2. 🔭 For that day, check **all future days** as potential selling days
3. 📊 Calculate the profit for every `(buy, sell)` pair
4. 🧠 Keep track of the **maximum profit seen** so far

This guarantees correctness because **every valid transaction** is evaluated.

### 🧩 Algorithm Steps
- Initialize `maxProfit = 0`
- Loop through each day as a buying day
- For each buying day:
    - Loop through all future days
    - Calculate `sellingPrice - buyingPrice`
    - Update `maxProfit` if the profit is higher
- Return `maxProfit`

### ⏱️ Complexity Analysis
- Time Complexity:	`O(n²)`
- Space Complexity:	`O(1)`