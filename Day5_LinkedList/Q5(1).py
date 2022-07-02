class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __del__(self):
        if(self.next):
            del self.next

def addTwoNumbers(head1,head2):
    # Node1 and Node2 point to the current node of the first and second list,respectively

    node1 = head1
    node2 = head2

    # SUMHEAD stores the head of the su  list
    sumHead = None
    prev = None

    # Sum and carry store the sum and carry geneated in the current iteration
    sum = carry =0

    while(node1 != None or node2 != None):
        sum = carry

        if(node1 != None):
            # Add the curent nodes value to the sum.
            sum += node1.next

            # Move to the next node of the list1
            node1 = node1.next

        if(node2 != None):
            # Add the curent nodes value to the sum
            sum += node2.data

            #Move to the next node of the list2
            node2 = node2.next

        # Createthe next node of the sum list
        sumNode = Node(sum%10)

        # Add the  node to the sum list
        if(sumHead == None):
            # Node generated is the first node. So, update the head of the sum list
            sumHead = sumNode
        else:
            # Add the node to end of the list
            prev = sumNode

            # Get the new carry
            carry = sum//10
    if carry > 0:
        # Carry is generated from the last iteration. So, add a new node.
        prev.next = Node(carry)
    
    return sumHead
    
