"""
Can search for values in O(log n) time just like an array
BSTs allow for insertion and deletion of values in O(log n) time, unlike a sorted asrray which would require O(n) time
The simplest way to traverse a tree is with recursion
All nodes to the left will be smaller and all nodes to the right will be larger
"""

def search(root, target):
    if not root:
        # a null node will cause a false return because the target was not located in the tree
        return False
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True