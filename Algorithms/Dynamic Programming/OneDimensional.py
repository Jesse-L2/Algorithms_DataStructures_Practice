"""GPT generated - summary of dynamic programming

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. 
It is applicable when the problem can be divided into overlapping subproblems that can be solved independently. 
The key idea is to store the results of these subproblems to avoid redundant computations, which is known as memoization. Dynamic programming is often used in optimization problems where the goal is to find the best solution among many possible ones.

There are two main approaches to dynamic programming:

1. Top-Down Approach (Memoization/Caching): This approach involves solving the problem recursively and storing the results of subproblems in a table (usually a dictionary or an array) to avoid redundant calculations.

2. Bottom-Up Approach (Tabulation): This approach involves solving all possible subproblems starting from the smallest ones and using their solutions to build up solutions to larger subproblems.

Dynamic programming is commonly used in problems involving sequences, such as the Fibonacci sequence, shortest path problems, and knapsack problems.
"""

def brute_force_fib(n): # O(n^2)
    if n <= 1:
        return n
    else:
        return brute_force_fib(n - 1) + brute_force_fib(n - 2)
    
def memoized_fib(n, cache): # top down appraoch, O(n) solution
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    # cache then return
    cache[n] = memoized_fib(n - 1, cache) + memoized_fib(n - 2, cache)
    return cache[n]

def dp(n): # bottom up approach, O(n) time complexity
    # start at base cases and calculate up
    # version only storing the 2 previous fib numbers, bringing space complexity down to O(1) because we are overwriting old numbers
    if n < 2:
        return n
    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]