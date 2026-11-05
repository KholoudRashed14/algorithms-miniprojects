# Algorithms Mini Projects

A collection of four small, focused projects. Each one takes a single algorithm or data structure from the Algorithms course and applies it to a concrete, easy-to-picture problem. The goal is to go beyond textbook pseudocode: implement it, test it, measure it, and explain why it works.

Every project lives in its own folder with:

- `main.py`: the implementation plus runnable test cases or demo
- `README.md`: the problem statement, the approach, complexity analysis, and sample output

---

## Table of Contents

- [Projects Overview](#projects-overview)
- [Project Details](#project-details)
  - [1. Sorting Benchmark Lab](#1-sorting-benchmark-lab)
  - [2. Max Profit Finder](#2-max-profit-finder)
  - [3. Task Scheduler](#3-task-scheduler)
  - [4. Top-K Frequent Words](#4-top-k-frequent-words)
- [Complexity Summary](#complexity-summary)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Concepts Covered](#concepts-covered)

---

## Projects Overview

| # | Project | Algorithm / Data Structure | Idea in one line |
|---|---------|----------------------------|------------------|
| 1 | [Sorting Benchmark Lab](01-sorting-benchmark-lab/) | Insertion Sort, Merge Sort, Quick Sort | A race between sorting algorithms on different kinds of input |
| 2 | [Max Profit Finder](02-max-profit-finder/) | Divide and Conquer (Maximum Subarray) | Find the best day to buy and the best day to sell |
| 3 | [Task Scheduler](03-task-scheduler/) | Max-Heap (INSERT / EXTRACT-MAX) | An OS-style scheduler that always runs the most important task first |
| 4 | [Top-K Frequent Words](04-top-k-frequent-words/) | Min-Heap of size k | Find the k most frequent words in a text |

---

## Project Details

### 1. Sorting Benchmark Lab

**Problem:** Which sorting algorithm is actually fastest, and does the answer change with the input?

**Approach:** Implement Insertion Sort, Merge Sort, and Quick Sort from scratch, then time each one on several input types (random, already sorted, reverse sorted, many duplicates) and a range of input sizes.

**What it shows:**

- Insertion Sort is fast on small or nearly sorted data but degrades to quadratic time on large inputs.
- Merge Sort gives a stable O(n log n) in every case, at the cost of extra memory.
- Quick Sort is usually the fastest in practice, but its worst case (bad pivots on sorted input) is O(n²).

| Algorithm | Best | Average | Worst | Extra space |
|-----------|------|---------|-------|-------------|
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

---

### 2. Max Profit Finder

**Problem:** Given a list of daily stock prices, find the best day to buy and the best day to sell later to maximize profit.

**Approach:** Convert the prices into daily price changes, then the answer becomes the **Maximum Subarray** problem: find the contiguous stretch of days with the largest total change. It is solved with **Divide and Conquer**:

1. Split the array into two halves.
2. The best subarray is either entirely in the left half, entirely in the right half, or **crosses the midpoint**.
3. Solve the two halves recursively and compute the crossing case in linear time.
4. Return the best of the three.

**Complexity:** T(n) = 2T(n/2) + O(n), which gives **O(n log n)** time.

---

### 3. Task Scheduler

**Problem:** Simulate how an operating system picks which task to run next when tasks have different priorities.

**Approach:** Store tasks in a **Max-Heap** keyed by priority.

- `INSERT`: add a new task and sift it up to restore the heap property.
- `EXTRACT-MAX`: remove and return the highest-priority task, then sift down to restore the heap property.

The most important task is always at the root, so picking the next task is instant.

**Complexity:**

| Operation | Time |
|-----------|------|
| Peek at highest priority | O(1) |
| Insert | O(log n) |
| Extract-Max | O(log n) |

---

### 4. Top-K Frequent Words

**Problem:** Given a text, return the k words that appear most often.

**Approach:**

1. Count the frequency of every word with a hash map.
2. Keep a **Min-Heap of size k** of (frequency, word) pairs.
3. For each word, push it onto the heap. If the heap grows beyond k, pop the smallest, so the heap always holds the k best seen so far.
4. At the end, the heap contains the answer.

**Why a Min-Heap?** The root is the weakest of the current top k, so it is exactly the element to evict when a better one arrives. This avoids sorting all unique words.

**Complexity:** O(n log k) time and O(n) space, which beats a full sort (O(n log n)) when k is much smaller than n.

---

## Complexity Summary

| Project | Core idea | Time |
|---------|-----------|------|
| Sorting Benchmark Lab | Compare sorting strategies | O(n²) vs O(n log n) |
| Max Profit Finder | Divide and Conquer | O(n log n) |
| Task Scheduler | Max-Heap | O(log n) per operation |
| Top-K Frequent Words | Min-Heap of size k | O(n log k) |

---

## Repository Structure

```
algorithms-mini-projects/
├── README.md
├── 01-sorting-benchmark-lab/
│   ├── main.py
│   └── README.md
├── 02-max-profit-finder/
│   ├── main.py
│   └── README.md
├── 03-task-scheduler/
│   ├── main.py
│   └── README.md
└── 04-top-k-frequent-words/
    ├── main.py
    └── README.md
```

---

## Getting Started

**Requirements:** Python 3.8 or newer. No external libraries are needed.

```bash
# Clone the repository
git clone https://github.com/KholoudRashed14/algorithms-mini-projects.git
cd algorithms-mini-projects

# Run any project
cd 01-sorting-benchmark-lab
python main.py
```

Each project's own README has the expected output so you can check your run against it.

---

## Concepts Covered

- Sorting algorithms and their trade-offs (time, space, stability)
- Divide and Conquer and recurrence relations
- Binary heaps: sift-up, sift-down, and priority queues
- Choosing the right data structure for the job (Max-Heap vs Min-Heap)
- Asymptotic analysis: best, average, and worst case
