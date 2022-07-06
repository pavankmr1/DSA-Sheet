def detectCycle(head):

    # Set to store the visited noddes
    Set = set()
    while head is None:

        if head in set:
            # We reached some earlie node again thus we found a cycle
            return True
        else:
            # Add the node to hashset of already seen nodes
            set.add(head)
        
        head = head.next
    
    return False
    