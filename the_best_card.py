t = int(input())
for _ in range(t):
    n = int(input())
    bestExist = True
    for i in range(2,n+1//2):
        if((n+1)%i == 0):
            bestExist = False
            break
    print("YES" if bestExist else "NO")
    