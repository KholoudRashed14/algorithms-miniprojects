"""
Meeting Rooms II
----------------
Given a list of meeting time intervals [start, end], find the minimum
number of conference rooms required so that no two meetings overlap
in the same room.

Approach: sort meetings by start time, then keep a min-heap of end times
(one entry per room currently in use). The heap root is the room that
frees up the earliest.
"""

import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])
    rooms = []  # min-heap of end times

    for start, end in intervals:
        # The earliest-ending meeting is over -> reuse its room
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)


def main():
    tests = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [2, 6], [3, 7], [4, 8]], 4),
        ([[1, 5], [5, 10]], 1),
        ([], 0),
    ]

    for intervals, expected in tests:
        result = min_meeting_rooms(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | intervals={intervals} -> rooms={result} (expected {expected})")


if __name__ == "__main__":
    main()
