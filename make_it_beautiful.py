t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if len(set(arr)) == 1:
        print("NO")
    else:
        arr.sort(reverse=True)
        print("YES")
        while arr[0] == arr[1]:
            arr.append(arr[0])
            arr.remove(arr[0])
        print(*arr)