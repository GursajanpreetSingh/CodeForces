n = int(input())
arr = list(map(int,input().split()))

crimes = 0
recruits = 0
for i in range(n):
    if(arr[i]==-1):
        if(recruits==0):
            crimes += 1
        else:
            recruits -= 1
    else:
        recruits += arr[i]

print(crimes)
    