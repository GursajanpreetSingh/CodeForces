t = int(input())
for _ in range(t):
    x,k = map(int,input().split())
    steps = []
    count = 0

    if(x%k==0):
        count = 2
        steps.append(x-1)
        steps.append(1)
    else:
        count = 1
        steps.append(x)

    print(count)
    print(*steps)