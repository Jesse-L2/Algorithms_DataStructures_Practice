# As simple as going from left to right: in-order traversal
# left to current node to right
# will visit every node 1 time so time complexity O(n)
# Depth first search is best implemented with recursion, but can be done iteratively with a stack

# def inOrderTraversal(root):
#     result = []
    

# all traversal methods are O(n) and are DFS (depth first search) where we go as deep as we can before visiting other subtrees
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def reverseorder(root):
    if not root:
        return
    reverseorder(root.right)
    print(root.val)
    reverseorder(root.left)