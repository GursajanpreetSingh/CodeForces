t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    no_steps = 0
    steps = []
    if n%2 == 0:
        no_steps = 2
        steps.append([1,n])
        steps.append([1,n])
    else:
        no_steps = 4
        steps.append([1,n-1])
        steps.append([1,n-1])
        steps.append([n-1,n])
        steps.append([n-1,n])
    print(no_steps)
    for i in steps:
        print(*i)
        
