t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if c % 2 == 0:
        if b >= a:
            winner = "Second"
        else:
            winner = "First"
    else:
        if a >= b:
            winner = "First"
        else:
            winner = "Second"
    print(winner)