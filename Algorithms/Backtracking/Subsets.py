def subsetsWithNoDuplicates(nums):
    subsets, currSet = [], [] # subsets contains sublist results
    helper(0, nums, currSet, subsets)
    return subsets

def helper(index, nums, currSet, subsets):
    if index >= len(nums):
        subsets.append(currSet.copy()) # use copy rather than reference originals
        return
    
    # TWO POSSIBLE DECISIONS:
    # 1) Include nums[index]
    currSet.append(nums[index])
    helper(index + 1, nums, currSet, subsets)
    currSet.pop()

    # 2) Don't include nums[index]
    helper(index + 1, nums, currSet, subsets)

def subsetsWithDuplicates(nums):
    nums.sort() # sort the input list to handle duplicates correctly (we put them all adjacent to each other)
    subsets, currSet = [], [] # subsets contains sublist results
    helper2(0, nums, currSet, subsets)
    return subsets

def helper2(i, nums, currSet, subsets):
    if i >= len(nums):
        subsets.append(currSet.copy())
        return

    # include nums[i]
    currSet.append(nums[i])
    helper2(i + 1, nums, currSet, subsets)
    currSet.pop()

    # DON'T include nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, currSet, subsets)