from dataclasses import dataclass
import re


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __del__(self):
        if(self.next):
            del self.next

def addTwoNumbersHelper(node1, node2,carry):
    if(node1 == None and node2 == None and carry == 0):
        return None
    
    # Val1 and Val2 store the data of the current npdes of the two linked lists.
    # Next1 and Next2 point to the node present after the curent nodes of the two linked lists.

    if(node1 == None):
        # List 1 is empty. so, consider the current node vlue as zero
        val1 =0
        # And the node after the current node as NULL
        next1 = None
    else:
        val1 = node1.data
        next1 = node1.next

    if(node2 == None):
        # List 2 is empty. so, consider the current node vlue as zero
        val2 =0
        # and the node after the current node as NULL
        next2 = None
    else:
        val2 = node2.data
        next2 = node2.next

    # Add the values in the current nodes along with the carry
    sum = val1 + val2 + carry

    # Create the next node of the sum list.
    sumNode = Node(sum%10)

    # Recursively call the function to generate the remaining nodes of the sum loist
    sumNode.next = addTwoNumbersHelper(next1, next2,sum//10)

    return sumNode

def addTwoNumbers(head1,head2):
    return addTwoNumbersHelper(head1,head2,0)



