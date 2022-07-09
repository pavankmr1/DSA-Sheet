from sys import stdin
import sys

sys.setrecursionlimit(10**7)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

left = None

def isPalindrome(head):

    global left

    # Assign left node as start of Linked List
    left = head
    
    # check if linked list is palindrome or not
    isPal = isPalindrome(head)

    return isPal

def isPalindrome(right):

    global left

    # Stop recursion when right reach end of Linked List
    if right is None:
        return None

    isPal = isPalindrome(right.next)

    '''
        If sub-list is not palindrome then no need to check for current left and right, return false.
    '''
    if not isPal:
        return False

    # Check if both left and right node value are same
    if left.data == right.data:
        isSame = True
    else:
        isSame = False 
    
    # Move left pointer to next node
    left = left.next

    return isSame

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


