def fourSum(arr,target):
    n = len(arr)
    ans =[]

    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if (arr[i]+arr[j]+arr[k]+arr[l]+arr[l])== target:
                        ans.append([arr[i],arr[j],arr[k],arr[l]])
    return ans