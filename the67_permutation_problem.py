t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    left = 1
    right = 3*n
    while(left < right):
        arr.append(left)
        arr.append(right)
        arr.append(right-1)

        left += 1
        right -= 2
    print(*arr)