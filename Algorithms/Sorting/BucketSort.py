# Runs in O(n) time worst case! But can only rarely be used due to constraints on buckets
# Works well with many duplicates
def bucket_sort(arr: list[int]) -> list[int]:
    # For example assuming only 3 values
    counts = [0, 0, 0, 0]
    # Count number of times value appears in arr
    for n in arr:
        counts[n] += 1
    
    # Fill original array
    i = 0
    for n in range(len(counts)):
        for _ in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
