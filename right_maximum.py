t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    itr = n
    maxi = arr[0]
    for i in range(n):
        if arr[i] >= maxi:
            maxi = arr[i]
        else:
            itr -= 1
    print(itr)