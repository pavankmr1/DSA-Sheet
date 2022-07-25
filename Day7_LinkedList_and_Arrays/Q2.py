class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

def cloneRandomListHelper(head, visitedHash):
    
    if head is None:
        return None

    '''
        If we have already processed the current node, 
        then we simply return the cloned version of it.
    '''
    if head in visitedHash.keys():
        return visitedHash.get(head)

    
    '''
        Create a new node with the label same
        as old node. (i.e. copy the node).
    '''
    node = LinkedListNode(head.data)
    
    '''
        Save this value in the hash map. This is needed
        since there might be loops during traversal due to 
        randomness of random pointers and this would
	    help us avoid them.
    '''

    visitedHash[head] = node

    '''
        Recursively copy the remaining linked list starting
        once from the next pointer and then from the random pointer.
	    Thus we have two independent recursive calls.
	    Finally we update the next and random pointers for the new node created.
    '''   

    node.next = cloneRandomListHelper(head.next,visitedHash)
    node.random = cloneRandomListHelper(head.random,visitedHash)

    return node

def cloneRandomList(head):

    '''
        HashMap which holds old nodes as keys
        and new nodes as its values.
    '''
    visitedHash = {}

    return cloneRandomListHelper(head,visitedHash)
