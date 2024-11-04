"""
Heaps can either be a Min Heap (smallest value at root node) or Max Heap (largest value at root node)
Priority queue can be made looking at either min or max first. Priority queues are implemented using a Heap which is a more common term
Duplicates are ok unlike binary tree
Root always puts at index 1 instead of 0 by convention
Order property (only with a complete binary tree):
left child = 2 * i
right child = 2 * i + 1
parent = i / 2 (round down)
"""

class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        # Time complexity is the height of the heap - O(log n)
        self.heap.append(val)
        i = len(self.heap) - 1

        # "Percolate up" (shift up while order property not satisfied)
        while self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # "Percolate down" (shift down while order property not satisfied)
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res


    