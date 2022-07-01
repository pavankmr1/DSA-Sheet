from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeKthNode(head,k):
    if head == None or k==0:
        return head
    
    # It sotres all the nodes of Linked list
    nodeList = []

    #creating temporary node
    temp = head

    # Iterating the Linked List.
    while temp is not None:
        # Add current node to list
        nodeList.append(temp)

        temp = temp.next

    # If head of linked list is Kth node
    if k == len(nodeList):
        next = head.next
        head.next = None
        head = next
    else:
        # Remove the Kth node from end
        nodeList[len(nodeList)-k-1].next = nodeList[len(nodeList)-k].next

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

# Main Code
if __name__ == '__main__':
    # k = int(input().strip())
    # arr = [int(i) for i in input().strip().split(' ')]
    arr = [1,2,3,4,5,6,7,8,9,10]
    k = 4
    head = build_linkedList(arr)
    res_head = removeKthNode(head,k)

    while res_head is not None:
        print(res_head.data, end=' ')
        res_head = res_head.next



