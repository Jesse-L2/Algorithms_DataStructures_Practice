# Find the middle of a linked list
def middleOfLinkedList(head):
    # Time: O(n) | Space: O(1)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Determine if a linked list has a cycle (revisits the same node twice)
def hasCycle(head):
    # Time: O(n) | Space: O(1)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Determine if a linked list has a cycle and return the head of the cycle else None
def hasCycleHead(head):
    slow, fast, slow2 = head, head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next: # reached end of linked list
        return None
    
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
        

