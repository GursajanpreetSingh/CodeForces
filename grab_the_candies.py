t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sum_odd = 0
    sum_even = 0
    for i in arr:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    if sum_even > sum_odd:
        print("YES")
    else:
        print("NO")
