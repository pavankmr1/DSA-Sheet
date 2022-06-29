# When traversing the list with a pointer slow, 
# make another pointer fast that traverses twice as fast.
#  When fast reaches the end of the list, slow must be in the middle.


def findMiddle(head):

    # If head is null just return null
    if(head is None):
        return head

    # If the Linked list has just 1 element, return element
    if(head.next is None):
        return head

    fast = head
    slow = head

    while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
    
    return slow