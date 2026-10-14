t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    result = []
    if n == 1:
        result.append(1)
    else:
        for i in range(n):
            result.append(2)
    print(*result)