def rotate(head, k):

    # Base condition
    if head == None:
        return head
    
    len = 1
    temp = head

    # Calculate length of the linked list.
    while temp.next != None:
        temp = temp.next
        len += 1

    # If k is greater, then k brings it in range of 0 -len
    if len < k:
        k = k % len

    k = len - k

    # Number of rotaations are same as len so no change in LL
    if k == len or k == 0:
        return head
    
    count =1
    current = head

    while count < k and current != None:
        current = current.next
        count +=1
    
    if current == None:
        return head
    
    # Changing Pointers
    temp.next = head
    head = current.next
    current.next = None

    return head
    
        