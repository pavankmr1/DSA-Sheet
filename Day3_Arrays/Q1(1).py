def findTargetInMatrix(matrix,m,n,target):
    i=0
    j=m-1
    while(i<n and j>=0):
        if(matrix[i][j]==target):
            return True
        elif(matrix[i][j]>target):
            j -=1
        else:
            i +=1

    return False

matrix = [[1, 2, 4], [6, 7, 8], [9, 10, 34]]
print(findTargetInMatrix(matrix,3,3,78))
