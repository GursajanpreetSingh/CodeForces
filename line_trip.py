t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    vols = []
    min_vol = a[0]
    for i in range(n-1):
        min_vol = max(min_vol,abs(a[i]-a[i+1]))
    min_vol = max(min_vol,2*abs(a[n-1]-x))
    print(min_vol)
