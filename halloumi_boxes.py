t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if(arr!=sorted(arr) and k==1):
        print("NO")
    else:
        print("YES")