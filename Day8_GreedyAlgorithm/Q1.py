# Custom class for storing starting time, finishing time and position of meeting

class meeting:
    def __init__(self,start,end,pos):
        self.start = start
        self.end = end
        self.pos = pos

# Function for finding maximum meeting in one room
def maxMeeting(l,n):

    # Intialise an array list for storing answer
    ans = []

    # storing of meeting according to their finish time
    l.sort(key=lambda x:x.end)

    # intially select the first meeting
    ans.append(l[0].pos)

    #time_limit to check whether new meeting can be conducted or not.
    time_limit = l[0].end

    # Check for all meeting whether it can be selected or not
    for i in range(1,n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
    
    # print  final slected meetings
    for i in ans:
        print(i+1,end=" ")
        
# Driver Code

if __name__ == '__main__':

    # Starting time
    s = [1,3,0,5,8,5]

    # Finish time
    f = [2,4,6,7,9,9]

    # Number of meetings
    n = len(s)

    l = []

    for i in range(n):

        # Creating object of meeting and adding in the list
        l.append(meeting(s[i],f[i],i))
    
    # Function call
    maxMeeting(l,n)