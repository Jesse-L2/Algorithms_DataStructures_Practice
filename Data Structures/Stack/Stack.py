"""Stack with Python list
S.push(e)	L.append(e)
S.pop()	L.pop()
S.top()	L[−1]
S.is_empty()	len(L) == 0
len(S)	len(L)

Operation	Running Time
S.push(e)	O(1)* amortized
S.pop()	    O(1)* amortized
S.top()	    O(1)
S.is_empty()O(1)
len(S)	    O(1)
"""

class ArrayStack():
    def __init__(self):
        """Create empty stack"""
        self._data = []

    def __len__(self):
        """Return num elements in stack"""
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to top of stack"""
        self._data.append(e)

    def peak(self):
        """Return but don't remove top element, Raise exception if empty stack"""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """Remove and return top element of stack (LIFO), Raise exception if empty stack"""
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()
