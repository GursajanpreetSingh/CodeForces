t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    if(arr[0]==arr[n-1]):
        print(-1)
    else:
        b = []
        c = []
        for el in arr:
            if(el==arr[0]):
                c.append(el)
            else:
                b.append(el)
        print(f"{len(b)} {len(c)}")
        print(*b)
        print(*c)
    