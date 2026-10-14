t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sit = 0
    for i in range(n):
        if arr[i] <= i+1:
            sit += 1
    print(sit)