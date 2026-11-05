# Task Scheduler (Max-Heap)

## Problem
An operating system has many tasks waiting to run, each with a priority. The CPU must always pick the **most important** task next. Scanning the whole list every time is slow, so we need a faster way to get the highest-priority task.

## Idea
Store the tasks in a **max-heap**: a binary tree where every parent is greater than or equal to its children, so the highest priority is always at the root.

The heap is stored in a plain list:
- parent of index `i` is `(i - 1) // 2`
- children of index `i` are `2i + 1` and `2i + 2`

## Operations
| Operation | What it does | Time |
|-----------|--------------|------|
| `INSERT` | Add the task at the end, then **sift up** until the heap property holds | O(log n) |
| `EXTRACT-MAX` | Take the root, move the last item to the root, then **sift down** | O(log n) |
| `PEEK` | Look at the root without removing it | O(1) |

The heap is implemented by hand (no `heapq`) to show how the algorithm works.

## Tie-breaking
Tasks with equal priority run in arrival order. Each task is stored as `(priority, -arrival_number, name, duration)`, so on a tie the earlier arrival compares as larger.

## Run
```bash
python main.py
```
No external libraries needed.

## Output
```
Scheduling order (highest priority first):
  t= 0 -> t= 1 | running Fix crash      (priority 10)
  t= 1 -> t= 3 | running Kernel update  (priority 9)
  t= 3 -> t= 7 | running Open browser   (priority 5)
  t= 7 -> t=10 | running Virus scan     (priority 5)
  t=10 -> t=12 | running Print report   (priority 3)
  t=12 -> t=15 | running Play music     (priority 2)
```
Tasks were added in a different order, but they run by priority. The two priority-5 tasks run in the order they arrived.

## Why a heap?
| Approach | Insert | Get highest |
|----------|--------|-------------|
| Unsorted list | O(1) | O(n) |
| Sorted list | O(n) | O(1) |
| **Max-heap** | **O(log n)** | **O(log n)** |

The heap balances both operations, which is what a scheduler needs.

## What I learned
- How a binary heap lives inside a simple list.
- How sift up and sift down keep the heap property in O(log n).
- Why a priority queue beats re-sorting every time a task arrives.
