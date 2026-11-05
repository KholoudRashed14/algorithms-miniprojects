# Max Profit Finder (Divide and Conquer)

## Problem
Given the price of a stock for each day, find the best day to **buy** and the best day to **sell** (buy must come before sell) to get the maximum profit.

## Idea
Convert the prices into **daily differences** (`price[i+1] - price[i]`).
The best profit is then the **maximum contiguous subarray** of these differences (the Maximum Subarray problem).

## Divide and Conquer approach
Split the array in half. The best subarray must be in one of three places:

1. **Entirely in the left half**: solve recursively.
2. **Entirely in the right half**: solve recursively.
3. **Crossing the midpoint**: scan left from the middle and right from the middle, then combine the best of each side.

The answer is the largest of the three. The recursion stops when a single element is left.

## Complexity
| Approach | Time |
|----------|------|
| Divide and Conquer | O(n log n) |
| Linear scan (for comparison) | O(n) |

Recurrence: `T(n) = 2T(n/2) + O(n)`, which gives `O(n log n)`.

## Run
```bash
python main.py
```
No external libraries needed.

## Output
```
Divide and Conquer:
  Buy on day 7 (price 63)
  Sell on day 11 (price 106)
  Profit = 43

Linear Scan:
  Buy on day 7, sell on day 11, profit = 43
```
Both methods agree, which confirms the divide-and-conquer result is correct.

## What I learned
- How to turn a stock problem into a Maximum Subarray problem.
- How the "crossing the midpoint" case is what makes divide and conquer work here.
- A faster O(n) solution exists, but the D&C version shows the technique clearly.
