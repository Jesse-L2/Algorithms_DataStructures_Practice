"""
Can search for values in O(log n) time just like an array
Technically you could call it O(h) time where h is the height of the Binary Search Tree
BSTs allow for insertion and deletion of values in O(log n) time, unlike a sorted asrray which would require O(n) time
The simplest way to traverse a tree is with recursion
All nodes to the left will be smaller and all nodes to the right will be larger
"""

from BinaryTree import TreeNode

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
    
def insert(root, val):
    # Insert a new node and return the root of the BST
    # log(n) time
    if not root:
        # val becomes root node
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def remove(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = remove(root.left, val)
    elif val > root.val:
        root.right = remove(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = minValueNode(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return root

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def maxValueNode(root):
    curr = root
    while curr and curr.right:
        curr = curr.right
    return curr