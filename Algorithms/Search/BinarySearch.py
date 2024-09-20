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