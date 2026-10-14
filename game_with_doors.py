t = int(input())
for _ in range(t):
    l,r = map(int,input().split())
    L,R = map(int,input().split())
    doors = 0
    if r < L or R < l:
        doors = 1
    elif r == L or R == l:
        doors = 2
    else:
        doors = min(r,R)-max(l,L)
        if min(l,L) < max(l,L):
            doors += 1
        if min(r,R) < max(r,R):
            doors += 1
    print(doors)
