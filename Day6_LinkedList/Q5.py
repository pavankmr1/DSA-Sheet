import numbers


def firstNode(head):

    # To keep track of number of nodes passed in the outer loop.
    numberOfNodesPassed = 0
    outerLoopNode = head

    while (outerLoopNode!= None):

        # Increment the count for current node.
        numberOfNodesPassed += 1
        outerLoopNode = outerLoopNode.next
        innerLoopNode = head
        counterForInnerLoop = numberOfNodesPassed

        while(counterForInnerLoop):
            # We found a repetitive Node/cycle
            if (innerLoopNode == outerLoopNode):

                # Current node of inner loop will be the starting point of cycle
                return innerLoopNode
            
            innerLoopNode = innerLoopNode.next
            counterForInnerLoop -= 1
    # We didnt find any cycle
    return None