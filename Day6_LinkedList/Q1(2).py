
from sys import stdin

# Parallel Traversal Approach
# Calculate the length of both the lists, say len1 and len2
# Get the absolute difference of the lengths, diff = |len1 – len2|
# Now traverse the long list from the first node till ‘diff’ nodes so that from there onwards both the lists have equal number of nodes
# Then traverse both the lists in parallel and check whether a common node is reached (Note that getting a common node is done by comparing the address of the nodes, not the data)
# If yes, return that node’s data
# If no, return -1

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head):
    length = 0
    while head != None:
        head = head.next
        length +=1
    return length

def findIntersection(head):

    # get the length of both list
    firstListLength = length(firstHead)
    secondListLength = length(secondHead)  
        
    # move headA and headB to the same start point
    while (firstListLength > secondListLength) :
        firstHead = firstHead.next  
        firstListLength-=1  
    
    
    while (firstListLength < secondListLength) :
        secondHead = secondHead.next  
        secondListLength-=1

    # find the intersection until end
    while (firstHead != secondHead) :
        firstHead = firstHead.next  
        secondHead = secondHead.next 

    if(firstHead == None) :
        return -1  
    
    return firstHead.data  

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1
    return head

def attach(head1 , head2) :
	temp1 = head1  

	while(temp1!= None and temp1.next != None) :
		temp1 = temp1.next  
	
	temp2 = head2  
	prev = None 
	
	
	while(temp2.next != None) :
		prev = temp2  
		temp2 = temp2.next  
	
	if(prev == None) :
		if(temp1.data == head2.data) :
			temp1.next = head2  
	
	else :
		if(temp2.data == temp1.data) :
			prev.next = temp1  
	
#main

head1 = takeInput()
head2 = takeInput()
head3 = takeInput()

attach(head1, head2)
#Create Intersection
temp1 = head1  
while(temp1.next != None) :
	temp1 = temp1.next  

temp1.next = head3  

ans = findIntersection(head1, head2)  

print(ans)
	 
    
    