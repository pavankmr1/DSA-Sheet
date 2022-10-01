import heapq

def getMedian(matrix):
    n = len(matrix)
    m = len(matrix[0])

    minHeap = []

    # Create Min Heap
    for j in range(n):
        heapq.heappush