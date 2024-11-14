"""
    Breadth First Search(BFS) is a fundamental graph traversal algorithm that begins with a node, then traverses all adjacent nodes. Once all adjacent nodes are visted, all of their adjacent nodes are traversed. Here we are traversing level by level. Djikstra's, Kahn's, and Prim's algorithms are based on BFS. 
"""

# Go layer by layer down the tree (better done iteratively than with recursion)
# aka level order traversal

from collections import deque # double ended queue

def breadthFirstSearch(root):
    # only traverses each node once despite having a for loop in a while loop so time complexity O(n)
    # space complexity O(n) because each node is stored once in a queue, worst case really half the size of the tree due to size of the last level
    queue = deque()

    if root:
        queue.append(root)
    
    level = 0
    while len(queue) > 0:
        print(f"level: {level}")
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

              