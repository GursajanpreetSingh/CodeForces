t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if a==b or b==c or c==a:
        print(0)
    else:
        arr = sorted([a,b,c])
        print(min(arr[2]-arr[1],arr[1]-arr[0]))