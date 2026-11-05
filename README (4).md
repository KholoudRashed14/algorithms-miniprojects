# 04 - Meeting Rooms (Min-Heap)

## Problem
Given an array of meeting time intervals `[start, end]`, return the **minimum number of conference rooms** required so that no two overlapping meetings share a room.

**Example**

```
Input:  [[0, 30], [5, 10], [15, 20]]
Output: 2
```

## Approach
1. Sort the meetings by start time.
2. Keep a **min-heap** of end times, one per room currently in use.
3. For each meeting:
   - If the earliest-ending meeting (heap root) finishes at or before the new meeting's start, pop it and reuse that room.
   - Push the new meeting's end time onto the heap.
4. The heap size at the end is the number of rooms needed.

## Complexity
| | Cost |
|---|---|
| Time | O(n log n): sorting plus heap operations |
| Space | O(n): the heap in the worst case |

## Run

```bash
python main.py
```

## Sample output

```
PASS | intervals=[[0, 30], [5, 10], [15, 20]] -> rooms=2 (expected 2)
PASS | intervals=[[7, 10], [2, 4]] -> rooms=1 (expected 1)
PASS | intervals=[[1, 5], [2, 6], [3, 7], [4, 8]] -> rooms=4 (expected 4)
PASS | intervals=[[1, 5], [5, 10]] -> rooms=1 (expected 1)
PASS | intervals=[] -> rooms=0 (expected 0)
```
