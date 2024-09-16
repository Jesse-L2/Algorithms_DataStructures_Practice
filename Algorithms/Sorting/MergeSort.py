def merge_sort(arr, l, r):
    if l - r + 1 <= 1:
        # Base case where len(arr) is <= 1
        return arr
    m = (l + r) // 2 # middle index

    # Sort left
    merge_sort(arr, l, m)
    # Sort right
    merge_sort(arr, m + 1, r)
    # Merge halfs
    merge(arr, l, r, e)

    return arr

def merge(arr, l, m, r):
    # Create temp arrays
    left = arr[l:m + 1]