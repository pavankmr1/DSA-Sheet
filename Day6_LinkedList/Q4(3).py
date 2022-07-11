import re
from sys import stdin

class Node:
    def __init__(self,data):

        self.data = data
        self.next = None

# Reverse the LinkedList

def reverse(head):

    current = head

    reverseHead = None

    while current is None:

        currentNext = current.next

        current.next = reverseHead

        reverseHead = current

        current = currentNext
    
    return reverseHead


def isPalindrome(head):
    slow = head
    fast = head
    prev = head

    # Find the middle node using Slow and fast pointer 
    while(fast is not None and fast.next is not None):
        
        prev = slow
        fast = fast.next.next
        slow = slow.next

    '''
        Fast pointer would become NULL when there are even elements in the list and
        not NULL for odd elements. We need to skip the middle node for odd case.
    '''

    if fast is not None:
        slow = slow.next

    # When there is only one node in given Linked List.

    if slow is None:
        return True

    # Dividing Linked list in two parts by pointing prev next to null.
    prev.next =None
    # Now reverse the second half
    reverseHead = reverse(slow)

    # Iterate through both Linked list and then compare it.
    while head is not None:
        if head.data != reverseHead.data:
            return False
        reverseHead = reverseHead.next
        head = head.next
    return True

def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        if currentData == -1:
            break
        
        Newnode=Node(currentData)
        
        if head is None:
            head=Newnode
            tail=Newnode
        else:
            tail.next=Newnode
            tail=Newnode
            
    return head







#Main
t = int(stdin.readline().rstrip())

while t > 0:
    
    head = takeinput()
    
    if isPalindrome(head):
        print('true')
    else:
        print('false')
        
    t -= 1

   
