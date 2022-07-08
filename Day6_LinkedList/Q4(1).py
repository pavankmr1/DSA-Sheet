from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):

    # Creating a temporary node
    temp = head

    # Creating Node for storing head of clone LinkedList
    cloneHead = None

    while temp is not None:

        newNode = Node(temp.data)
        newNode.next = cloneHead
        cloneHead = newNode
        temp = temp.next
    
    while head is not None:
        # check ifboth node value is same or not
        if head.data != cloneHead.data:
            return False
        
        head = head.next
        cloneHead = cloneHead.next
    return True

def takeinput():
    
    inputlist=[int(ele) for ele in input().split()]
    
    head=None
    tail=None
    
    for currentData in inputlist:
        
        
        
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



