from turtle import clone


class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

def clonedRandomList(head):

    # Initialise two references, one with original list's head.
    origCurr = head
    cloneCurr = None

    '''
        Hash map which contains node to node 
        mapping of original and clone linked list.
    '''
    mapp ={}

    '''
        Traverse the original list and make
        a copy of that in the clone linked list.
    '''
    while origCurr is not None:

        cloneCurr = LinkedListNode(origCurr.data)
        mapp[origCurr]= cloneCurr
        origCurr = origCurr.next

    origCurr =  head

    '''
        Traversal of original list again to adjust the next
	    and random references of clone list using hash map.
    '''
    while origCurr != None:

        cloneCurr = mapp.get(origCurr,None)
        cloneCurr.next = mapp.get(origCurr.next)
        cloneCurr.random = mapp.get(origCurr.random)
        origCurr = origCurr.next
    
    # Return the head reference of the clone list.
    ans = mapp.get(head,None)
    return ans
    
