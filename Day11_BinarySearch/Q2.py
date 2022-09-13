def getMedian(matrix):

    n= len(matrix)
    m= len(matrix[0])

    data = []

    for i in range (n):
        for j in range (m):
            data.append(matrix[i,j])
    
    data.sort()

    return data[(m+n)//2]