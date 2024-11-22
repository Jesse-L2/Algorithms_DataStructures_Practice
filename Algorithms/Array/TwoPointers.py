def checkPalindrome(string):
    """
    Check if an array is a palindrome in O(n) time
    """
    # create a pointer on each end, increment first and decrement second, constantly checking if they are equal
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

print(checkPalindrome('abba'), checkPalindrome('abcd'))

def findIndices(nums, target):
    """
    Given a sorted input array, return the two indices containing elements that sum to the target value. Assume only one solution exists.
    Time Complexity O(n)
    """
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left, right]

nums1 = [1, 2, 3, 4, 6]
target1 = 6
print(findIndices(nums1, target1))  # Expected output: [1, 3]

nums2 = [2, 3, 4, 5, 9]
target2 = 7
print(findIndices(nums2, target2))  # Expected output: [0, 3]
