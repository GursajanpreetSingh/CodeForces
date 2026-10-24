t = int(input())
for _ in range(t):
    n = int(input())
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    else:
        arr = [1,2,3]
        for i in range(3,n):
            arr.append(arr[-1]*2)
        print(*arr)
    