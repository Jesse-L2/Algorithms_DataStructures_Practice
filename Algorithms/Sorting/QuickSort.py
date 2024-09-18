def quick_sort(arr: list[int], start, end) -> list[int]:
    # Pick a pivot, usually the last value as we will do here
    # Any value less than or equal to pivot gets put in left side
    # Other values (bigger values) go in the right side
    # Perform in place, O(1) space
    if end - start + 1 <= 1:
        return arr
    pivot = arr[end]
    left = start

    # Partition
    for i in range(start, end):
        if arr[i] <= pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    arr[end] = arr[left]
    # move pivot to the value that the left pointer got to
    arr[left] = pivot

    # Sort left
    quick_sort(arr, start, left - 1)
    # Sort right
    quick_sort(arr, left + 1, end)

    return arr