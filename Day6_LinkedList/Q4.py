from sys import stdin

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def isPalindrome(head):
    
    # It stores the Linked list node value
    st = []

    # Creating temporary Node
    temp = head

    while temp is not None:

        # Add the current node value to the stack
        st.append(temp.data)

        # Move currentpointer to next node
        temp = temp.next
    
    while head is not None:

        # Get the top most element of stack
        top = st.pop()

        if top != head.data:
            return False
        head = head.next
    return True

def takeInput():

    inputlist =[int(ele) for ele in input().split()]

    head = None
    tail = None

    for currentData in inputlist:

        Newnode = Node(currentData)

        if head is None:
            head = Newnode
            tail = Newnode
        else:
            tail.next = Newnode
            tail = Newnode
    return head

# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()

    if isPalindrome(head):
        print('True')
    else:
        print('False')  
    
    t -=1


