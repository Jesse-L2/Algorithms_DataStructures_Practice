# Types - Matrix, Adjacency Matrix, Adjacency List
# Nodes are referred to as verices and the pointers that connect the nodes are referred to as edges
# In a matrix, 0 is used to represent an empty node and 1 is used to represent a full or blocked node
# The space complexity of a matrix is O(n * m) where n is the number of rows and m is the number of columns

# Matrix Depth First Search (DFS) is similar to tree traversal. 
matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

def dfs(matrix, r=0, c=0, visited=None):
    # Base cases - 1) going out of bounds (ex: matrix[-2][2]) 2) revisiting a node we have already visited 3) If the current coordinate is 1 (no path through that coordinate). For any of these cases, we will return a 0 denoting that there is not a unique path.
    # If we reach the right most column and bottom most row, then we have found a valid path, return 1
    # Use a hash set to track visited coordinates (has O(1) lookups unlike a list)
    # from any given coordinate r, c, we can perform DFS on r+1, c; r-1, c; r, c+1; r, c-1. If call returns 1, add to count, else if returns 0, do not add to count
    ROWS, COLS = len(matrix), len(matrix[0])
    
    if visited is None:
        visited = set()

    if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or matrix[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    visited.add((r, c))
    count = 0
    count += dfs(matrix, r+1, c, visited)
    count += dfs(matrix, r-1, c, visited)
    count += dfs(matrix, r, c+1, visited)
    count += dfs(matrix, r, c-1, visited)
    visited.remove((r, c))

    return count

print(dfs(matrix))
    
class GraphNode: # Adjacency List
    def __init__(self, val):
        self.val = val
        self.neighbors = []