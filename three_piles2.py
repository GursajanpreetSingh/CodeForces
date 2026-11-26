t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    arr = sorted([a,b,c])
    if(arr[2]==arr[1]+1 and arr[1]==arr[0]+1):
        print("YES")
    else:
        print("NO")