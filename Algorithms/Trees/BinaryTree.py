"""
Each node in the tree will have two pointers to its children, one on the left and one on the right.
The final node (leaf) of the tree will still have two pointers, but to null rather than other nodes
Height - path from node to deepest leaf
Depth - path from node to root node
Building the tree is O(n log n)
"""

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None