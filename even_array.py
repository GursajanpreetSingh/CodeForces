t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    we = 0
    wo = 0
    for i in range(n):
        if i % 2 == arr[i] % 2:
            continue
        elif i%2 == 0:
            we += 1
        else:
            wo += 1
    if we == wo:
        print(we)
    else:
        print(-1)
