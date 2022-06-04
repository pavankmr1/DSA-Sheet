def findTargetInMatrix(mat, m, n, target):
    # considering elemnets in the matrix as a linear array ,therfore the length of the matrix would be (M X N)-1
    start, end =0,m*n-1

    #performing Binary Search for matrix elements

    while start <= end:

        mid = start +(end-start)//2
        # mid//n = row index , mid%n = column index
        # { 0 1 2
        #   3 4 5 
        #   6 7 8 }
        # m= 3 n=3 3 X 3 matrix
        #if mid = 4 then mid//n = 4//3 = 1 = row index
        #                mid%n  = 4%3 =  1 = column index
        # mat[1][1] is 4th element of the matrix

        val = mat[mid//n][mid%n]

        if target < val :
            end = mid-1
        elif target > val :
            start = mid+1
        else :
            return True
    
    return False

matrix = [[1, 2, 4], [6, 7, 8], [9, 10, 34]]
print(findTargetInMatrix(matrix,3,3,78))
