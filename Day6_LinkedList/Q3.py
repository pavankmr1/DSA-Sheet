from locale import currency
from tkinter import N


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def getListAfterReverseOperation(head,n,b):
    # If linked list is empty, return head of the linked list
    if head is None:
        return None
    
    # Variable to keep track of current index in the block array.
    idx = 0

    cur,prev,temp = head,None, None
    tail, join = None,None
    isHeadUpdated = False

    # Reverse nodes until the list is empty or entire block array has been considered
    while(cur != None and  idx <n):

        # K represents the size of the current block
        k = b[idx]

        # just move to the next block if size of the current bl0ck is zero
        if k==0:
            idx+=1
            continue

        join = cur
        prev = None

        # Reverse nodes until end of list is reached or current block has been reversed
        while (cur != None and k>0):
            k -=1
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

            # Update the head pointer when reversing the first block.
            if (isHeadUpdated == False):
                head = prev
                isHeadUpdated = True
            
            # Tail pointer keeps track of the last node before the current k-reversed linked list
            # We join the tail pointer with the current k-reversed linked list's head
            if tail != None:
                tail.next = prev

            # The tail is then updated to the last node of the current k-reversed linked list
            tail = join
            idx +=1

        # If entire block is iterated and reached at end, then we append the remaining nodes to the tail of the partial modified linked list
        if tail != None:
            tail.next = cur
        
        return head
        