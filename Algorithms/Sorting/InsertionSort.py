def insortion_sort(arr):
    """
    Input: An array of n comparable integer elements
    Output: A sorted array of the same n elements in non-decreasing order
    Time Complexity: O(n^2) - worst case, O(n) - best case
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # right element is less than left
            temp = arr[j + 1] # store right
            arr[j + 1] = arr[j] # assign value of right to left
            arr[j] = temp # assign value of left to right
            j -= 1 # move j back and check the previous element
        return arr


        # ALTERNATIVE IMPLEMENTATION
        # curr = arr[k]
        # j = k
        # while j > 0 and arr[j - 1] > curr:
        #     arr[j] = arr[j - 1]
        #     j -= 1
        # arr[j] = curr