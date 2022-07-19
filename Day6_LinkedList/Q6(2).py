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
    
