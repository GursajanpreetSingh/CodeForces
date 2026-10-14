t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ops = 0
    ops += arr.count(0)
    if arr.count(-1) %2 != 0:
        ops += 2
    print(ops)