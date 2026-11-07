t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    arr = [a,b,c]
    arr.sort()
    if(arr[2]==arr[0]+arr[1]):
        print("YES")
    else:
        print("NO")


