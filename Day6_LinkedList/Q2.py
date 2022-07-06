def detectCycle(head):
    numberOfNodesPassed = 0
    outerLoopNode = head

    # Iterating over the Linked-list

    while(outerLoopNode != None):

        numberOfNodesPassed +=1
        outerLoopNode = outerLoopNode.next
        innerLoopNode = head
        counterForInnerLoop = numberOfNodesPassed

        # Iterating again from the beginning
        while(counterForInnerLoop):

            # We found a repetitive Node/cycle
            if innerLoopNode == outerLoopNode:
                return True
            
            innerLoopNode = innerLoopNode.next
            counterForInnerLoop -=1

    # We didnt found any Cycle
    return False

