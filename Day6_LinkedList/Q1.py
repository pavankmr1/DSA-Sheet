from sys import stdin

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findIntersection(firstHead,secondHead):

    temp1 = firstHead

    # For every noe of first list, traverse the second list and check if is the intersection
    while temp1!=None:
        temp2 = secondHead
        while temp2!=None:

            if temp1 == temp2:
                return temp1.data
            temp2 = temp2.next
        temp1 = temp1.next
    
    # if there is no intersection, return-1
    return -1

# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i=0
    while(i < len(datas)) :
        data = data[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        i+=1
    return head

def attach(head1,head2):
    temp1 = head1

    while(temp1!= None and temp1.next != None):
        temp1 = temp1.next
    temp2 = head2
    prev = None

    while temp2.next != None:
        prev = temp2
        temp2 = temp2.next
    if prev == None:
        if temp1.data == head2.data :
            temp1.next = head2
    else:
        if(temp2.data == temp1.data):
            prev.next = temp1


# Main
head1 = takeInput()
head2 = takeInput()
head3 = takeInput()

attach(head1,head2)
# Create Intersection
temp1 = head1
while(temp1.next != None):
    temp1 = temp1.next
temp1.next = head3

ans = findIntersection(head1,head2)

print(ans)
            

