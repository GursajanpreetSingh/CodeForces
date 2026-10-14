t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    org_arr = []
    l = 0
    r = n-1
    while(l<=r):
        if l==r:
            org_arr.append(arr[l])
        else:
            org_arr.append(arr[l])
            org_arr.append(arr[r])
        l+= 1
        r-= 1
    print(*org_arr)