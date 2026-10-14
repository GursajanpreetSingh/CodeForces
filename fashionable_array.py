t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = []
    while arr:
        unique = sorted(set(arr),reverse=True)

        for x in unique:
            ans.append(x)
            arr.remove(x)
        
    print(*ans)