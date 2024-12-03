# Find the middle of a linked list
def middleOfLinkedList(head):
    # Time: O(n) | Space: O(1)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
