def rotate(head, k):
    # Base Condition
    if head == None:
        return head
    
    len = 1
    temp = head

    # Calculate length of linked list
    while temp.next != None:
        temp = temp.next
        len += 1
    
    k = k % len

    # Number of rotations are same as len so no cange in LL
    if len ==k or k ==0:
        return head
    
    temp = head

    for i in range (0, abs(len-k-1),1):
        temp = temp.next
    
    # Changing Pointers
    head = temp.next
    temp.next = None

    return head