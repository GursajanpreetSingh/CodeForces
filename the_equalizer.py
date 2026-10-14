t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if sum(arr) %2 != 0:
        print("YES")
    else:
        if k*n % 2 == 0:
            print("YES")
        else:
            print("NO")