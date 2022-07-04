import re
from sys import stdin

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findIntersection(firstHead,secondHead):

    # Set to store reference of first head
    Set = set()

    temp = firstHead

    while(temp != None):
        set.add(temp)
        temp = temp.next

    # If set is empty that means there is no first list then there would be no intersection
    if(len(Set)==0):
        return -1

    temp = secondHead

    while(temp != None):
        if (temp in Set) :
            return temp.data
        temp = temp.next
    return -1

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