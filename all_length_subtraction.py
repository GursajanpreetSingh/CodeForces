t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    left = 0
    right = n-1
    flag = True
    for i in range(n):
        if i+1 == arr[left]:
            left += 1
        elif i+1 == arr[right]:
            right -= 1
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")