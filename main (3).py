import re
from collections import Counter


class Entry:
    """A (word, count) pair. 'Smaller' means weaker: lower count, or on a tie,
    alphabetically later. So the heap root is always the weakest candidate."""

    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        return self.word > other.word


class MinHeap:
    """Min-heap stored in a list. Parent of i is (i-1)//2, children are 2i+1 and 2i+2."""

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def peek(self):
        return self.data[0]

    def push(self, item):
        """Add at the end, then sift up. O(log k)."""
        self.data.append(item)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def pop(self):
        """Remove the smallest item (the root), then sift down. O(log k)."""
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return top

    def replace_root(self, item):
        """Replace the root with a new item and sift down. O(log k)."""
        self.data[0] = item
        self._sift_down(0)

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest


def top_k_frequent(text, k):
    """Return the k most frequent words as [(word, count), ...], best first.
    Ties are broken alphabetically."""
    words = re.findall(r"[a-z']+", text.lower())
    counts = Counter(words)

    heap = MinHeap()                      # never holds more than k entries
    for word, count in counts.items():
        entry = Entry(word, count)
        if len(heap) < k:
            heap.push(entry)              # still free chairs
        elif heap.peek() < entry:         # new word beats the weakest one
            heap.replace_root(entry)

    result = []
    while len(heap) > 0:
        e = heap.pop()
        result.append((e.word, e.count))
    result.reverse()                      # weakest came out first, so flip
    return result


if __name__ == "__main__":
    text = """
    the quick brown fox jumps over the lazy dog the dog barks
    and the fox runs away the quick fox is quick and the dog is lazy
    """
    k = 3
    print(f"Top {k} most frequent words:")
    for rank, (word, count) in enumerate(top_k_frequent(text, k), start=1):
        print(f"  {rank}. {word:<6} -> {count} times")
