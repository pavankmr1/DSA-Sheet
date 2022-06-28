# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialise next as null

# Linked list class contains a Node object
class LinkedList:

    # Function to initialize the linked list head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning of the list
    def push(self, new_data):

        #1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)

        #3. Make next of new Node as head
        new_node.next = self.head

        #4. Move the head to point to new node
        self.head = new_node

    # This function is in linked list class. Inserts a
    # new node after the given prev_node. This method is 
    # defined inside LinkedList classshown above.
    def insertAfter(self, prev_node,new_node):

        #1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return

        #2&3. Create a new node and  put in the data
        new_node = Node(new_node)

        #4. Make the next of new nodde as next of prev_node
        new_node.next = prev_node.next

        #5. make next of prev_node as new_node
        prev_node.next = new_node

    # This function is defined in Linked List Class
    # Appends a new node at the end. This method is
    #defined inside LinkedList class shown above
    def append(self, new_data):

        #1. Create a new node
        #2. Put in the data
        #3. set next as None
        new_node = Node(new_data)

        #4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        #5. Else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next
        
        #6. Change the next of last node
        last.next = new_node

    # Utility function to print the Linked List
    def printList(self):
            temp = self.head
            while(temp):
                print(temp.data,end = " ")
                temp = temp.next

#Code execution starts here...
if __name__ == "__main__":

    # Start with the empty list
    llist = LinkedList()

    # Insert 6. So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the begining. so linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the begining. so linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. so linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8 after 7. So linked List becomes 1->7->8->6->4->None
    llist.insertAfter(llist.head.next,8)

    print('Created linked list is: ')
    llist.printList()

# Time complexity: O(n)
# Space Complexity:O(1)
    