def firstNode(head):
    # To keep track of visited nodes
    nodesSeen = set()

    while head != None:
        if (head in nodesSeen):

            # We reached some earlier node again thus we found a cycle and current node is starting point.
            return head
        
        else:
            # Add the node to hashset of already seen nodes
            nodesSeen.add(head)
        head = head.next
    
    return None
    