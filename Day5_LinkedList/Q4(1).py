from distutils.dep_util import newer
import re


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def removeKthNode(head,k):

    if head is None or k ==0:
        return head

    # It stores length of the linked list
    L=0

    # Creating temporary node.
    temp = head

    # iterating over the list
    while temp is not None:
        L= L+1
        temp = temp.next
    
    # If head of Linked List is Kth node
    if k== L:
        next = head.next
        head.next = None
        head = next
    else:
        countNode = 0
        temp = head

        while temp is not None:
            countNode +=1

            # Remove the Kth node form end of the list
            if(L-k == countNode):
                temp.next = temp.next.next
                break
            temp = temp.next

    return head

def build_linkedList(arr):
    head = None

    for i in range(len(arr)):

        new = Node(arr[i])

        if head is None:
            head = new
            tail = new
        else:
            tail.next = new
            tail = tail.next

    return head

if __name__ == "__main__":
    # k = int(input().strip())
    # arr = [int(i) for i in input().strip().split(' ')]
    arr = [1,2,3,4,5,6,7,8,9,10]
    k = 4
    head = build_linkedList(arr)
    res_head = removeKthNode(head,k)

    while res_head is not None:
        print(res_head.data, end=' ')
        res_head = res_head.next
