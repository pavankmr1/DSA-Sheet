class Solution(object):
    
    def calPascal(self,i,j):
        if  j==0 or j==i:
            return 1
        else:
            return self.calPascal(i-1,j-1)+self.calPascal(i-1,j)
    
    def generate(self,numRows: int)-> list:
        triangle =[]
        for i in range(numRows):
            add=[]
            for j in range(i+1):
                add.append(self.calPascal(i,j))
            triangle.append(add)
        return triangle

ob1 = Solution()
print(ob1.generate(5))
