t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    odds = 0
    for i in range(n):
        if arr[i] % 2 != 0:
            odds += 1
    if odds % 2 == 0:
        print("YES")
    else:
        print("NO")