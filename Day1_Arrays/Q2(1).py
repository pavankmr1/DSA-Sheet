class Solution():
    def generate(self,numRows):

        triangle =[]
        for i in range(numRows):
            add=[]
            for j in range(i+1):
                if i==j or j==0:
                    add.append(1)
                else:
                    add.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(add)
        return triangle
ob1 = Solution()
print(ob1.generate(5))
