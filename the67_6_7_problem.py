t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(len(arr)-1):
        arr[i] = -1 * arr[i]
    result = sum(arr)
    print(result)