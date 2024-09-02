#in the greedy question we have children with a certain greed
#that a child will only accept i or greater than i amount of 
# cookies and we have another array of cookies which is the amount of 
# cookies we have, we have to find the number of children whose greed
# we will be able to satisfy
def greedy(greed, cookies):
    n = len(greed)
    m = len(cookies)
    l = 0
    r = 0
    greed.sort()
    cookies.sort()
    while(l<m and r<n):
        if(greed[r]<=cookies[l]):
            r+=1
        l+=1
    return r


# this question says that we have changes of 5,10 and 20
# and each lemonade is 5 dollars and how can we sell all lemonades
# we have changes array which is the amount customer is giving 
# for example for array [5,5,5,10,20] first customer gives 5, we can sell
# second and third customer also gives 5 so we can sell
# fourth customer gives 10 we have to give 5 change, we have 3 fives 
# so we can sell to customer, now we have two 5's and one 10
# fifth customer gives 20 and we can either give change as one 10 and two 5's
# or three 5's , we have one 10 and two 5's thus we sold all lemonades
def lemonade(changes):
    five = 0
    tens = 0
    twenty = 0
    for i in range(len(changes)):
        if(changes[i]==5):
            five+=1
        elif(changes[i]==10):
            if(five):
                tens+=1
                five-=1
            else:
                return False
        else:
            if(tens and five):
                tens-=1
                five-=1
            elif(five>=3):
                five-=3
            else:
                return False
    return True
#print(lemonade([5,5,5,10,20]))


# in OS we have an algorithm called as shortest job first and 
# it is the scheduling policy that selects the waiting process
# with the smallest execution time to the largest execution time
def shortest_job_first(processes):
    processes.sort()
    t = 0
    wait_time = 0
    for i in range(len(processes)):
        wait_time +=t     
        t+=processes[i]
    return t//len(processes)
print(shortest_job_first([4,3,7,1,2]))

def jump_game(arr):
    maxIndex = 0 
    reached = False
    for i in range(len(arr)):
        if(maxIndex==0):
            return False
        else:
            maxIndex += arr[i]
    return True
print(jump_game([1,2,4,1,1,0,2,5]))
    
