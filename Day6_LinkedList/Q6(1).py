import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None
    
    def __del__(self):
        if self.next:
            del self.next


class NodevaluePair:

    def __init__(self,node,value):
        self.value = value
        self.node = node

def flattenLinkedList(head):
    setattr(NodevaluePair,"__lt__",lambda self,other: self.value <= other.value)

    pointer = head
    result = None

    # Heap to store all the node value pair
    pq = []

    # Push the head nodes
    while pointer != None:
        temp = NodevaluePair(pointer,pointer.data)
        heapq.heappush(pq, temp)
        pointer = pointer.next
    
    # Add child nodes while popping out the minimum
    while len(pq) != 0:
        current = heapq.heappop(pq)
        temp = current.node

        # If the child of temp is not NULL push it to the heap
        if temp.child != None:
            curr = NodevaluePair(temp.child,temp.child.data)
            heapq.heappush(pq,curr)

        if result == None:
            result = temp
            pointer = temp
            pointer.next = None
        else:
            pointer.child = temp
            pointer = temp
            pointer.next = None
    
    return result




# Time Complexity
# O( log(N) * (N * K)), where 'N’ denotes the size of the linked list and ‘K’ is the average number of child nodes for each of the N nodes.

 

# Since, every node in the linkedlist is traversed once and log(N) is the time taken to min-heapify the queue so the total complexity will be O(N * log(N)) + O(((N * K) - N) * log(N)) = O( log(N) * (N * K)) 

# Space Complexity
# O(N), where ‘N’ denotes the size of the linked list 

 

# Since we are using a priority queue to store the top horizontal nodes and at any instant heap will not contain more than N nodes..

