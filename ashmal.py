t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input().split())
    s = a[0]
    for i in range(1,n):
        if a[i]+s < s+a[i]:
            s = a[i]+s
        else:
            s += a[i] 
    print(s)
    
