from heapq import heapify, heappush,heappop

# Creating empty MaxHeap
MaxHeap = []
heapify(MaxHeap)

# Adding items to the(MaxHeap using heapush function 
heappush(MaxHeap, 10)
heappush(MaxHeap,30)
heappush(MaxHeap,20)
heappush(MaxHeap,400)

# printing the value of minimum element
print("Head value of MaxHeap:"+ str(MaxHeap[0]))
print("\n")

# Printing the element of the MaxHeap
print("The MaxHeap elements are:")
for i in MaxHeap:
    print(i, end= ' ')
print("\n")

element = heappop(MaxHeap)


# printing the elemnts of the MaxHeap
print("Theheap elements are: ")
for i in MaxHeap:
    print(i, end= ' ')
print("\n")


# MAX HEAP


MaxHeap = []
heapify(MaxHeap)

# In python there is no MAxHeap we should implement it using MinHeap so
# Adding items to the heap using heappush function by multiplying them with -1

heappush(MaxHeap, -1 * 10)
heappush(MaxHeap, -1 * 30)
heappush(MaxHeap, -1 * 20)
heappush(MaxHeap, -1 * 400)

# printing the value of maximum element
print("Head value of heap : " + str(-1 * MaxHeap[0]))
print("\n")
# printing the elements of the heap
print("The MaxHeap elements : ")
for i in MaxHeap:
    print((-1*i), end=" ")
print("\n")
 
element = heappop(MaxHeap)
 
# printing the elements of the heap
print("The MaxHeap elements : ")
for i in MaxHeap:
    print(-1 * i, end = ' ')
print("\n")


