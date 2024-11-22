""" 
Prefix Sum Array - aka a cumulative sum array. Each element represents a running sum of all elements up to that index in the original array
Ex: [2, -2, 3, -5, 4] -> [2, 0, 3, -1, 3]
"""

class PrefixSum:
    # Allows calculation of the sum of any subarray starting at the left and ending at the right in O(1) time with prefix[right] - prefix[left - 1]
    def __init__(self, nums):
        self.prefix = []
        total = 0
        # Build in O(n) time
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight, preLeft)
    
class PostfixSum:
    def __init__(self, nums):
        self.postfix = []
        total = 0
        # Build in O(n) time, iterating from the end to the start
        for n in reversed(nums):
            total += n
            self.postfix.append(total)
        
        self.postfix.reverse() # Reverse the postfix list to maintain the order

    def rangeSum(self, left, right):
        postLeft = self.postfix[left]
        postRight = self.postfix[right + 1] if right + 1 < len(self.postfix) else 0
        return (postLeft, postRight)
