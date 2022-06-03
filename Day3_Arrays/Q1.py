from sys import stdin
def findTargetInMatrix(mat, m, n, target):
    for i in range(m):
        for j in range(n):
            if mat[i][j] == target:
                return True
    return False

#arr = list(map(int,stdin.readline().strip().split(" ")))
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findTargetInMatrix(arr,3,3,3))