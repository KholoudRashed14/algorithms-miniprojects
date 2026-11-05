# Top-K Frequent Words (Min-Heap)

## Problem
Given a text, find the `k` most frequent words. Sorting every distinct word costs O(n log n), which is wasteful when `k` is small (for example, the top 10 words of a huge book).

## Idea
Keep a **min-heap of size k** that holds the best `k` words seen so far. The root is the **weakest** of them, so it is the only one we ever need to compare against.

Think of it as a contest with `k` chairs:
- If a free chair exists, the word sits down.
- If all chairs are taken, the new word is compared with the weakest one. If it is stronger, it takes that seat. Otherwise it is ignored.

## Steps
1. Split the text into words and count them with `collections.Counter`.
2. For each `(word, count)`:
   - heap has fewer than `k` items: **push** it.
   - heap is full and the word beats the root: **replace the root** and sift down.
3. Pop everything from the heap. It comes out weakest first, so reverse it.

The min-heap is implemented by hand (no `heapq`) to show how it works.

## Tie-breaking
If two words have the same count, the alphabetically earlier word ranks higher. This makes the output deterministic.

## Complexity
Let `n` = number of distinct words.

| Approach | Time | Extra space |
|----------|------|-------------|
| Sort all words | O(n log n) | O(n) |
| **Min-heap of size k** | **O(n log k)** | **O(k)** |

Each heap operation costs O(log k) because the heap never grows past `k`.

## Run
```bash
python main.py
```
Only the standard library is used.

## Output
```
Top 3 most frequent words:
  1. the    -> 6 times
  2. dog    -> 3 times
  3. fox    -> 3 times
```
`dog` and `fox` both appear 3 times, so they are ordered alphabetically.

## What I learned
- Why the heap for "top k largest" is a **min**-heap: the root is the item to beat.
- How limiting the heap to size `k` improves on full sorting.
- How to define tie-breaking rules inside the comparison itself.
