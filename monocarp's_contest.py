t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ops = 0
    no_of_zeroes = arr.count(0)
    if(no_of_zeroes >= 2):
        if(arr[0]!=0):
            ops += 1
        if(arr[n-1]!=0):
            ops +=1
    else:
        ops = -1
    print(ops)