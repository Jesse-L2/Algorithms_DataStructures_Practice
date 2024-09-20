# Can only run on an input that is already in sorted order!
def binary_search(arr: list[int], target) -> list[int]:
     """
    Input: An array of n comparable integer elements
    Output: The index of the target element if found, -1 otherwise
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """
     left = 0
     right = len(arr) - 1
     while left <= right:
        # below is better than mid = (left + right) // 2 because will integer overflow at ~1 billion elements in the array
        mid = left + ((right - left) // 2)


        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return mid
        return -1
     
def binary_range_search(low, high):
    while low <= high:
        mid = low + (high - low) // 2
        
        if is_correct(mid) > 0:
            high = mid - 1
        elif is_correct(mid) < 0:
            low = mid + 1
        else:
            return mid
        
    return -1

max_value = 100

def is_correct(n):
    # Returns 1 if n too big, -1 too small, 0 if correct
    if n > max_value:
        return 1
    elif n < max_value:
        return -1
    else:
        return 0