from typing import List


def subset(i: int, sum: int, num: List[int], ans: List[int]) -> None:

    # Completerly travere the whole array, insert the "sum " in the "ans" list

    if i == len(num):
        ans.append(sum)
        return
    
    # Insert the element in the sum
    subset(i+1,sum+num[i], num, ans)

    # Dont take the elemnt in the sum
    subset(i+1,sum,num, ans)


def subsetSum(num: List[int]) -> List[int]:
    ans = []

    subset(0,0,num, ans)

    ans.sort
    
    return ans
    