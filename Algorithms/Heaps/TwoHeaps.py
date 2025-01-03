# can insert in O(log n) time rather than O(n) time by using a max heap for small values and a min heap for large values

# Implement a median finder where new values are inserted to the set a function getMedian() is returned from that set

# arbitrarily assign first value to maxHeap and then assign values based on that assignment

import heapq

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
    
    def insert(self, num) -> None:   # heap insertion is O(log n) time
        # First push to max heap and then swap with min heap if needed
        # python does not natively have a max heap so we get around that with a min heap and multiplying by -1
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Handle uneven sized heaps
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,  -1 * val)

    def getMedian(self) -> float: # O(1) time because reading from heap rather than popping
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        # If number of elements is even, return average of middle two numbers
        return (-1 * self.small[0] + self.large[0]) / 2
