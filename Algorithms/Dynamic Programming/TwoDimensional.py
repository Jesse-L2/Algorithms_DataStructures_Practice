# Count the number of unique paths from the top left to the bottom right. You can only move down or to the right.

# Brute Force - Time Complexity - O(2 ^ (n + m))
def bruteForce(row, col, rows, cols):
    if row == rows or col == cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    return (bruteForce(row + 1, col, rows, cols) + bruteForce(row, col + 1, rows, cols))

print(bruteForce(0, 0, 5, 5))

# Memoization Solution: Time Complexity - O(n * m)
def memoized(row, col, rows, cols, cache):
    if row == rows or col == cols:
        return 0
    if cache[row][col] > 0:
        return cache[row][col]
    if row == rows - 1 and col == cols - 1:
        return 1

    cache[row][col] = (memoized(row + 1, col, rows, cols, cache) + memoized(row, col + 1, rows, cols, cache))
    return cache[row][col]

print(memoized(0, 0, 5, 5, [[0] * 5 for i in range(5)]))
