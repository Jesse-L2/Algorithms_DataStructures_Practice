def merge_sort(arr: list[int], l, r) -> list[int]:
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
    right = arr[m + 1: r + 1]

    i = 0 # left index
    j = 0 # right index
    k = l # arr index

    # Merge both sorted halfs into the original array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Cases where elements remain in either half
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1