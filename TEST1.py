def reverseNumber(n):
    ans = 0
    while n>0:
        ans = n%10 + 10*ans
        n = n//10
    return ans
def pythagorianTriplet(x,y,z):
    a = max(x,max(y,z))
    b,c = 0,0
    if(a==x):
        b = y
        c= z
    if(a==y):
        b = x
        c = z
    if(a==z):
        b = x
        c = y
    if(b*b + c*c - a*a ==0):
        return True

def maximumSum(arr,n):
    curr = 0
    max_till_now = float('-inf')
    for i in range(n):
        curr+=arr[i]
        if(curr<0):
            curr = 0
        else:
            max_till_now = max(curr,max_till_now)
    return max_till_now
'''
curr = 0
max_till_now = float('-inf')
for i in range(n):
curr += arr[i]
if(curr<0):
curr = 0
else:
max_till_now = max(curr, max_till_now)
return max_till_now
'''
def transpose2D(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp 

def binaryToDecimal(n):
    x = 1
    ans = 0 
    while(n>0):
        y = n%10
        ans += x*y
        x *= 2
        n = n/10

def binaryToDecimal(n):
    x = 1
    ans = 0
    while(n>0):
        y = n%10
        ans += x*y
        x *= 2
        n = n/10

n = 12345
print(reverseNumber(n))
