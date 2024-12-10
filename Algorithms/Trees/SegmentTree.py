# root represents range for entire array and then we break those into smaller and smaller portions of the array
# on updating, can't just update a single value, also have to update that entire side of the chain of the tree (Time | O(log n))

# kind of similar to merge sort in breaking into equal halves
# add left and right indices and divide by 2 for midpoint
# can query a range by adding some of L and R children

class SegmentTree: # implemented with linked pointers, but could also be done with arrays
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    @staticmethod
    def build(nums, L, R): # O(n) time complexity
        if L == R: # base case where L and R are index same node
            return SegmentTree(nums[L], L, R)
        
        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root