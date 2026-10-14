t = int(input())
for _ in range(t):
    n = int(input())
    colors = list(map(int,input().split()))
    unique = len(set(colors))
    colors.sort()
    last = 0
    for item in colors:
        if item >= unique:
            last = item
            break
    print(last)