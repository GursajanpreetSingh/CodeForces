t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 2:
        if abs(arr[0] - arr[1])  > 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")