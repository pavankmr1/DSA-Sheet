import sys
from sys import stdin

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def sort(first,second):

    # when only one node is in first list, point its head ti the second list.
    if first.next == None:
        first.next = second
        return first

    cur1 = first
    next1 = first.next

    cur2 = second
    next2 = second.next

    while(next1 != None and next2 != None):
        if((cur2.data) >=(cur1.data) and (cur2.data)<=(next1.data) ):
            next2 = cur2.next
            cur1.next = cur2
            cur2.next = next1

            cur1 = cur2
            cur2 = next2
        elif(next1.next != None):

            # If there are more nodes in first list.
            
                next1 = next1.next
                cur1 = cur1.next

        # else point the last node of first list to the remaining nodes of econd list
        else:

            next1.next = cur2
            return first
    
    return first

def sortTwoLists(first, second):
    if first == None:
        return second
    if second == None:
        return first
    if(first.data < second.data):
        return sort(first,second)
    else:
        return sort(second,first)

def ll(arr):

    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head

    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):

    while head:

        print(head.data, end =" ")
        head = head.next


# arr1 = list(map(int, sys.stdin.readline().strip().split(" ")))
# arr2 = list(map(int, sys.stdin.readline().strip().split(" ")))
arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

l1 = ll(arr1[:])
l2 = ll(arr2[:])


l = sortTwoLists(l1, l2)

printll(l)
