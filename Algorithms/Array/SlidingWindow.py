"""
Given an array, return true if there are two elements within a window of size k that are equal
"""
def findWindowDuplicates(nums, k):
    window = set()
    left = 0
    
    for right in range(len(nums)): # iterate through all
        if right - left + 1 > k: # if the window is full, remove left and move left to the right by 1
            window.remove(nums[left])
            left += 1
        if nums[right] in window: # check if the right number added is in the hash set, if yes, return True and stop
            return True
        window.add(nums[right]) # add right element to hashset

    return False