t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    floor = 1
    last_apar = 2
    while(True):
        if n <= last_apar:
            print(floor)
            break
        floor += 1
        last_apar += x
            