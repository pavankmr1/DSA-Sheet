def countPaths(i,j,n,m,dp):
    if i == (n-1) and j== (m-1): return 1
    if i>=n or j>=m: return 0
    if(dp[i][j]!=-1): return dp[i][j]
    else:
        dp[i][j] = countPaths(i+1,j,n,m,dp)+countPaths(i,j+1,n,m,dp)
        return dp[i][j] 

n =3
m=3
dp = [[0 for i in range(n)] for j in range(m)];
print(countPaths(0,0,n,m,dp));