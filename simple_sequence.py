t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    for i in range(n,0,-1):
        result.append(i)
    print(*result)