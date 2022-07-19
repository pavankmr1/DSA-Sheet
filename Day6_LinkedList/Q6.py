from hashlib import new


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.child = None
    def __del__(self):
        if self.next:
            del self.next

def flattenLinkedList(root):

    answer = []

    # Traverse the linked list and add all the nodes to the array
    while root != None:

        answer.append(root.data)
        temp = root

        # Add all the child nodes
        while (temp.child != None):
            answer.append(temp.child.data)
            temp = temp.child
        root = root.next
    
    answer.sort()

    head = None
    tail = None

    # Create new linked list
    for i in range(len(answer)):
        newNode = Node(answer[i])
        if head == None:
            head = newNode
        else:
            tail.child = newNode
        tail = newNode
    return head

# Time Complexity
# O((N * K) * (log(N * K))), where ‘N’ denotes the size of the linked list and ‘K’ is the average number of child nodes for each of the N nodes. 

 

# Since we are taking all nodes data in an array and then sorting it so the total complexity will O(N * K) + O((N * K) * log(N * K))

# Space Complexity
# O(N * K), where ‘N’ denotes the size of the linked list and ‘K’ is the average number of child nodes for each of the N nodes. 

 

# Since we are using an array to store all the nodes of the linked list, and we are creating a new linked list to again store all the nodes, so the effective space complexity would be O(N * K) + O(N * K) = O(N * K).


    
