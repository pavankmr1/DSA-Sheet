class Solution:
    def calPascal(self,i,j):
        if  j==0 or j==1:
            return 1
        else:
                return calPascal(i-1,j-1)+calPascal(i-1,j)
    def generate(self,numRows) ->list[list[int]]:
        triangle =[]
        for i in range(numRows):
            add=[]
            for j in range(numRows+1):
                add.append(self.calPascal(i,j))
            triangle.append(add)
        return triangle

ob1 = Solution()
print(ob1.generate(5))