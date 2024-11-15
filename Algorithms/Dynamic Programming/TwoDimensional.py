# Count the number of unique paths from the top left to the bottom right. You can only move down or to the right.

# Brute Force - Time/Space Complexity - O(2 ^ (n + m))
def bruteForce(row, col, rows, cols):
    if row == rows or col == cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    return (bruteForce(row + 1, col, rows, cols) + bruteForce(row, col + 1, rows, cols))

# print(bruteForce(0, 0, 5, 5))

# Memoization Solution: Time/Space Complexity - O(n * m)
def memoized(row, col, rows, cols, cache):
    if row == rows or col == cols:
        return 0
    if cache[row][col] > 0:
        return cache[row][col]
    if row == rows - 1 and col == cols - 1:
        return 1

    cache[row][col] = (memoized(row + 1, col, rows, cols, cache) + memoized(row, col + 1, rows, cols, cache))
    return cache[row][col]

# print(memoized(0, 0, 5, 5, [[0] * 5 for i in range(5)]))

# Bottom up approach - we start with the base case solution and calculate each row one by one
def dpApproach(rows, cols): # Time Complexity - O(n * m); Space Complexity - O(m) (m is # cols)
    prev_row = [0] * cols

    for row in range(rows - 1, -1, -1): # stop at -1 position and go backwards
        curr_row = [0] * cols
        curr_row[cols - 1] = 1
        for col in range(cols - 2, -1, -1):
            curr_row[col] = curr_row[col + 1] + prev_row[col]
        prev_row = curr_row

    return prev_row[0] # return top left cell

# print(dpApproach(5, 5))
