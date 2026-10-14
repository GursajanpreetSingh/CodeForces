def score(suneet_card,salvic_card):
    if suneet_card > salvic_card:
        return 1
    elif salvic_card > suneet_card:
        return -1
    else:
        return 0
t = int(input())
for _ in range(t):
    a1,a2,b1,b2 = map(int,input().split())
    ways = 0
    if score(a1,b1) + score(a2,b2) > 0:
        ways += 2
    if score(a1,b2) + score(a2,b1) > 0:
        ways += 2
    
    print(ways)
    