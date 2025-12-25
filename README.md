# [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150) 📈💰

You’re given an array `prices`, where each number represents the price of a stock on a particular day. You can make **at most one transaction** — that means you can **buy once** and **sell once**.  

The catch? You have to **buy before you sell** ⬆️⬇️. Your profit is just the difference between the selling price and the buying price. If there’s no way to make money 💸, just return `0`.

---

### Example 📝
- **prices:** `[7,1,5,3,6,4]`  
  **Output:** `5` 💵  
  *Buy on Day 2 (price = 1) and sell on Day 5 (price = 6)*  

- **prices:** `[7,6,4,3,1]`  
  **Output:** `0` ❌  
  *Prices keep decreasing, so no profit is possible*

---

### Constraints ⚠️
- `1 ≤ prices.length ≤ 10⁵` 🗓️  
- `0 ≤ prices[i] ≤ 10⁴` 💲  

---

### Approaches 🔍

- #### [Brute Force](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock/tree/Approach_01-Brute_Force) 🐢
  Check **every possible pair** of buy and sell days 🔄, calculate the profit for each pair 📊, and keep track of the **maximum profit** 🏆.  
  Simple, correct ✅, but **O(n²)** time complexity ⏳.  

- #### [Greedy / Optimized](https://github.com/madiv9820/Best_Time_to_Buy_and_Sell_Stock/tree/Approach_01-Brute_Force) 🚀
  Traverse the prices **once** 👀, keeping track of the **lowest buying price so far** 🔻.  
  For each day, calculate profit if sold today 💵, and update the **maximum profit** 🏆.  
  Fast and efficient: **O(n)** time ⏱️ and **O(1)** space 🧠.  
---