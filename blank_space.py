t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    maxi = 0
    for el in arr:
        if el==0:
            maxi+= 1
        else:
            maxi = 0
        ans = max(maxi,ans)
    print(ans)