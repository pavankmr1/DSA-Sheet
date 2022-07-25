class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

# This function clones a given linkedlist
def cloneRandomList(head):
    
    curr = head
    temp = None

    # Insert additional node after every node of original data
    while curr != None:
        temp = curr.next

        # Inserting Node
        curr.next = LinkedListNode(curr.data)
        curr.next.next = temp
        curr = temp
    
    curr = head

    # Adjust the random pointers of the newly added nodes.
    while curr != None:
        if curr.next != None:
            if curr.random is not None:
                curr.next.random = curr.random.next
        
        # Move to the next newly added node by skipping an original node.
        if curr.next != None:
            curr = curr.next.next
        else:
            curr = curr.next

        original = head
        copy = None

        if head != None:
            copy = head.next

        # Save the start of copied linked list.
    temp = copy
    
    # Now separate the original list and copied list.
    while original != None and copy != None:
        
        if original.next != None:
            original.next = original.next.next
            
        if copy.next != None:
            copy.next = copy.next.next
            
        original = original.next
        copy = copy.next
        
    return temp  
