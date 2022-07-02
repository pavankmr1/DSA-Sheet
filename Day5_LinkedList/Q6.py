from hashlib import new


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Construtor to initialize  head
    def __init__(self):
        self.head = None
    
    # Function to insert a new node at the beginning
    def push(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    # Give a reference to the head of the linked list
    # and a position, delete the node at a given position
    def deleteNode(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index =0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    # utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d " % (temp.data),end=" ")
            temp = temp.next
 
 
# Driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(4)
print ("\nLinked List after Deletion at position 4: ")
llist.printList()
 


    