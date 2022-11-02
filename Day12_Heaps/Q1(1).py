from queue import PriorityQueue

def kthSmallLarge(arr,n,k):
    # Build Min-Heap from the given array
    minHeap = PriorityQueue()
    for val in arr:
        minHeap.put(val)
    
    # Pop from Min-Heap exactly k-1 times
    for i in range(1,k):
        x = minHeap.get()

    # Build MaxHeap from the given array
    maxHeap = PriorityQueue()
    for val in arr:
        # Inserting the values with neagative priority because maxHeap is implemented using negative of min heap
        maxHeap.put((-val, val)) 

    # Pop from Max Heap eactly k-1 times
    for i in range(1,k):
        maxHeap.get()
    
    result = [minHeap.get(), maxHeap.get()[1]]
    
    return result