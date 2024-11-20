"""
A greedy/dynamic programming algorithm that is used on an array to calculate the maximum sum subarray ending at a particular position, running in O(n) time
Lets us check if part of a series of numbers is negative and if so, stop bothering to compare to other subarrays
"""

def kadanesAlgo(nums):
    maxSum = nums[0]
    currSum = 0

    for num in nums:
        currSum = max(currSum, 0)
        currSum += num
        maxSum = max(currSum, maxSum)

    return maxSum