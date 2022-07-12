from tkinter import N


def firstNode(head):
    if head == None:
        # Empty linked list
        return None
    # Slow Pointer - This will be incremented by 1 node
    slow = head
    # Fast Pointer - This will be incremented by 2 nodes
    fast = head

    while True:
        if fast and fast.next:
            fast = fast.next.next
        else:
            # Fast pointer reached the end of the list.
            return None
        slow = slow.next
        if fast == slow:
            break
    slow = head

    # To track the position of node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
    
