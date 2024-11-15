"""
First understand input, output, constraints, and edge cases (ex: empty array, array contains only 1 element, all elements are the same, array contains duplicates, the array contains either very large or very small numbers, some numbers are negative, some numbers positive while some are negative, array is already sorted, target element is not present in the array, the array contains a lot of elements, intervals in the problem may overlap)
"""

# Common Patterns

# 1) Sliding Window - used for problems involving subarrays or substrings
# Ex: Find the maximum sum of subarray with size k
test_maxsum_arr = [-1, 2, 3, 0, -2, 4, 2, -1, 4, 0, 0, 1]
def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, 0
    for i in range(len(arr)): # Add elements to window until window size k full
        window_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - k + 1] # slide the window by (remove first element and add the next)
    return max_sum
print(max_sum_subarray(test_maxsum_arr, 4))

# 2) Two Pointers - used for either problems involving comparisons between two lists 
# Ex: Merge two sorted arrays
arr1 = [1, 2, 4, 6] # len = 4
arr2 = [3, 5, 7, 8]

def merge_sorted_arrays(arr1, arr2):
    # Compare elements from arr1[i] & arr2[j]
    i, j, result = 0, 0, []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

print(merge_sorted_arrays(arr1, arr2)) # [1, 2, 3, 4, 5, 6, 7, 8]