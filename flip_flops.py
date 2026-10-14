t = int(input())
for _ in range(t):
    n,c,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if c>= a[i]:
            if k > 0:
                to_add = min(k,c - a[i])
                a[i] += to_add
                k -= to_add
            c += a[i]
    print(c)