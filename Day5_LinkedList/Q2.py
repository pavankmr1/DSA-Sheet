def findMiddle(head):

    # Take a Pointer 'p' to traverse the linked list, initially pointing to head node
    p = head

    # Take a variable 'numberOfNodes' to count the number of nodes in the list
    numberOfNodes = 0

    # Count the nodes
    while(p.next is not  None):
        numberOfNodes += 1
        p = p.next
    
    mid = numberOfNodes/2

    # Find the mid node
    ptr = head
    while(mid>0):
        ptr = ptr.next
        mid = mid-1
    return ptr
    