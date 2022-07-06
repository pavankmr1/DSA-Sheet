def detectCycle(head):
    if head == None or head.next == None:
        return False
    
    # Slow pointer - This will be incremented by 1 Node
    slow = head

    # Fast Pointer - This will be incremented by 2 Nodes
    fast = head.next

    while slow != fast:
        # We reached the end of the list and havent found any Cycle
        if fast == None or fast.next == None:
            return False
        
        slow = slow.next
        fast = fast.next.next
    return True
    