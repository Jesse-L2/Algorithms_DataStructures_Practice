"""First in, first out (FIFO)
Operation	Running Time
Q.enqueue(e)	O(1) amortized
Q.dequeue()	O(1) amortized
Q.peak()	O(1)
Q.is_empty()	O(1)
len(Q)	O(1)
"""

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def peak(self):
             if self.is_empty():
                  raise Exception('Queue is empty')
             return self._data[self._front]
    
    def dequeue(self):
         """Remove and return first element, return exception if empty"""
         # front is an integer that represents the index of the first element of the queue
         if self.is_empty():
              raise Exception('Queue is empty')
         element = self._data[self._front]
         self._data[self._front] = None
         self._front = (self._front + 1) % len(self._data)
         self._size -= 1
         return element
    
    def enqueue(self, e):
        """Add e to back of queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, capacity):
        """Resize to new list of capacity >= len(self)"""
        
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

         
