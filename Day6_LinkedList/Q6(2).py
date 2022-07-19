class Node:
    def __init__(self,data):

        self.data = data
        self.next = None
        self.child = None
    
    def __del__(self):
        if self.next:
            del self.next

def merge(first,second):

    # If the first is None return second
    if first == None:
        return second
    
    # If the second is None return first
    if second == None:
        return first
    
    if first.data < second.data:
        merged = first
        merged.child = merge(first.child, second)
    else:
        merged = second
        merged.child = merge(first,second.child)

    return merged

def flattenLinkedList(head):
    if head == None or head.next == None:
        return head

    # Recur on next node
    head.next = flattenLinkedList(head.next)

    head = merge(head, head.next)

    return head

#     Time Complexity
# O(N * K), where ‘N’ denotes the size of the linked list and ‘K’ is the average number of child nodes for each of the N nodes. 

 

# Since, every next-node and every child node in the linkedlist is traversed only once, the final complexity would be O(N * K).

# Space Complexity
# O(N), where ‘N’ denotes the size of the linked list.

 

# Since for every call on a horizontal node each child sublist is called so the stack in recursion will always at most have N stacks .

