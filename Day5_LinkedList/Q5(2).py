class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __del__(self):
        if(self.next):
            del self.next

def addTwoNumbers(head1,head2):
    # Node1 and Node2 point to the current nodde of the first and seconf list respectively
    node1 = head1
    node2 = head2

    prev = None

    # Sum and carry store the sum and carry generated in the curent iteration
    sum = carry = 0

    while(node1 != None and node2 != None):
        # Add the values in the current nodes along with the carry
        sum = node1.data + node2.data + carry

        # Store the next node of the sum list in the current node of the first linked list
        node1.data = sum % 10

        # Get the new carry
        carry = sum// 10

        # keep track of the previous node
        prev = node1

        # Move to the next node
        node1 = node1.nexxt
        node2 = node2.next

    # If there are remaining digits in any one of the lists, add them to the sum list
    if (node1 != None or node2!= None):
        if(node2 != None):
            prev.next = node2

        node1 = prev.next

        while(node1 != None):
            # add the values in the current node along woth the carry
            sum = node1.data + carry
            #store the next node of the sum list in the current node of the first linked list
            node1.data = sum % 10
            # get the new carry
            carry = sum // 10
            # Keep track of the previous node
            prev = node1
            # Move to the next node
            node1 = node1.next

        if (carry>0):
            # carry is generated from the list iteration. So add a new node
            prev.next = Node(carry)  

    # Return the head of the sum list
    return head1