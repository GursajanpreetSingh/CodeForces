t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if len(set(arr)) < n:
        print(-1)
    else:
        arr.sort(reverse=True)
        print(*arr)