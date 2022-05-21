class Solution(object):
    def setZeroes(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        """>>> Example to understand R & C
        a=[[1,5,6,8],[1,2,5,9],[7,5,6,2]]
        >>> len(a)
        3 = R
        >>> len(a[0])
        4 = C 
        """
        rows,cols = set(), set()  
        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
    
    # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j]=0
        return matrix
ob1 = Solution()
print(ob1.setZeroes([[1,0,1],[1,1,1],[1,1,1]]))