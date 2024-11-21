def findFixedWindowDuplicates(nums, k):
    """
    Given an array, return true if there are two elements within a window of size k that are equal
    Time Complexity O(n)
    """
    window = set()
    left = 0
    
    for right in range(len(nums)): # iterate through all
        if right - left + 1 > k: # if the window is full, remove left and move left to the right by 1
            window.remove(nums[left])
            left += 1
        if nums[right] in window: # check if the right number added is in the hash set, if yes, return True and stop
            return True
        window.add(nums[right]) # add right element to hashset

    return False # no duplicates

def findVariableSizeWindowDuplicates(nums):
    """
    Find the length of the longest subarray that contains the same value in each position
    Time Complexity O(n)
    """
    left = 0
    length = 0
    for right in range(len(nums)):
        if nums[left] != nums[right]:
            left = right # set left to right index (slide window)
        length = max(length, right - left + 1)
    return length

def findSumGreaterOrEqualTarget(nums=[2,2, 1, 2, 3, 3], target=5):
    """
    Find the minimum length subarray containing a sum equal or greater than given target. Assume all values positive.
    Time complexity O(n) despite nested loops because worst case is running through for loop and then the while loop one time so O(2 * n) -> O(n)
    """
    left, length, total = 0, float('inf'), 0 

    for right in range(len(nums)):
        total += nums[right]

        if total >= target:
            length = min(length, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if length == float('inf') else length # if no valid subarray found return 0