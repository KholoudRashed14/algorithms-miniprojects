class MaxHeap:
    """Max-heap stored in a list. Parent of i is (i-1)//2, children are 2i+1 and 2i+2."""

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def insert(self, item):
        """INSERT: add at the end, then sift up. O(log n)."""
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def extract_max(self):
        """EXTRACT-MAX: remove the root, move the last item to the root, sift down. O(log n)."""
        if self.is_empty():
            raise IndexError("extract_max from an empty heap")
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return top

    def peek(self):
        return self.data[0]

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] > self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            largest = i
            if left < n and self.data[left] > self.data[largest]:
                largest = left
            if right < n and self.data[right] > self.data[largest]:
                largest = right
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest


class Scheduler:
    """OS-style scheduler: always runs the highest-priority task first.
    Equal priorities run in arrival order (first come, first served)."""

    def __init__(self):
        self.heap = MaxHeap()
        self.counter = 0  # arrival order, used to break ties

    def add_task(self, name, priority, duration):
        # Tuple comparison: higher priority wins; on a tie, the SMALLER counter
        # (earlier arrival) wins, so we store -counter.
        self.heap.insert((priority, -self.counter, name, duration))
        self.counter += 1

    def run(self):
        clock = 0
        while not self.heap.is_empty():
            priority, _, name, duration = self.heap.extract_max()
            start, clock = clock, clock + duration
            print(f"  t={start:>2} -> t={clock:>2} | running {name:<14} (priority {priority})")


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.add_task("Play music", 2, 3)
    scheduler.add_task("Kernel update", 9, 2)
    scheduler.add_task("Open browser", 5, 4)
    scheduler.add_task("Virus scan", 5, 3)
    scheduler.add_task("Print report", 3, 2)
    scheduler.add_task("Fix crash", 10, 1)

    print("Scheduling order (highest priority first):")
    scheduler.run()
