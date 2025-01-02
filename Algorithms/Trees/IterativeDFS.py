"""
3 main ways to traverse a tree: 1) Inorder 2) Preorder 3) Postorder
Time complexity is O(1) at each node with n being the number of nodes, so overall complexity is O(n) or O(h) where h is the height of the tree
"""

# Inorder traversal involves visiting: 1) The left child and its entire subtree 2) the current node 3) the right child and its entire subtree
# declare a curr pointer that points to the node currently being processed. Once curr points at a node, add it to a stack. Next, update curr to be curr.left. If curr points to null, we can pop it from the stack and print the node's value and then traverse the right subtree

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def inorder(root):
    stack = []
    curr = root

    while curr or stack: # basically going down tree until hitting a null 
        if curr: # if we have a node, add to stack and make curr the next node
            stack.append(curr)
            curr = curr.left
        else: # we don't have a node left to traverse in the tree so we start popping from stack
            curr = stack.pop()
            print(curr.value)
            curr = curr.right # set pointer to right child and then run it on entire right subtree

# Preorder traversal involves

def preorder(root):
    stack = []
    curr = root
    while curr or stack:
        if curr:
            print(curr.value)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()

# Postorder traversal involves traversing the left child, the right child, and then the root. It requires two stacks, visit and stack. visit and stack will always be the same size. stack will be used to store the nodes we are currently processing, while visit will keep track of whether we have previously visited the corresponding node in the stack
# Pop from stack and visit and if curr is not null, then we have not visited the node. 

def postorder(root):
    stack = [root]
    visit = [False]
    while stack:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                print(curr.value)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)