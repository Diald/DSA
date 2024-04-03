def permutations(arr):
    if len(arr)==0:
        return [[]]
    n = len(arr)
    ans = []
    for i in range(n):
        current = arr[i]
        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            ans.append([current]+perm)
    return ans
arr = [1,2,3]
print(permutations(arr))
