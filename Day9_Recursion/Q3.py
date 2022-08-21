from copy import deepcopy

def findSubsetsThatSumToKHelper(arr, ans, curSubset,k,idx):
    if idx == len(arr):
        if k==0 and len(curSubset) != 0:
            ans.append(curSubset)

    
    # Case when we do not include the current element in the subset
    curSubsetCopy = deepcopy(curSubset)
    findSubsetsThatSumToKHelper(arr,ans, curSubsetCopy,k,idx+1)

    # Case when we include the current  element in the subset
    curSubset.append(arr[idx])
    findSubsetsThatSumToKHelper(arr,ans, curSubset, k-arr[idx], idx+1)

def findSubsetsThatSumToK(arr,n,k):

    # List  to store the subsets that sum to k
    ans = []

    # List to store the current subset
    curSubset = []
    findSubsetsThatSumToKHelper(arr,ans, curSubset,k,0)

    return ans
    
