t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    curr = arr[0]
    for i in range(1,n):
        if curr > arr[i]:
            count += 1
        else:
            curr = arr[i]

    print(count)