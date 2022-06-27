# Method 1 (Simple : O(n3)): We can consider all substrings one by one and check for each substring whether 
# it contains all unique characters or not. There will be n*(n+1)/2 substrings. Whether a substring contains all unique characters or not
#  can be checked in linear time by scanning it from left to right and keeping a map of visited characters.
def areDistinct(str,i,j):
    # Note : Default values in visited are false
    visited = [0] * (26) #if we consider the dtring contains only alphabets ,since there are 26 so *26

   # for k in range(len(str)):


