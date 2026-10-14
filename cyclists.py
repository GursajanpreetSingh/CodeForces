t = int(input())
for _ in range(t):
    n,k,p,m = map(int,input().split())
    costs = list(map(int,input().split()))
    plays = 0
    win_cost = costs[p-1]
    if n==k:
        plays = m//win_cost
    else:
        while(m >= win_cost):
            if p<=k :
                plays += 1
                m -= win_cost
                costs.pop(p-1)
                costs.append(win_cost)
                p = n
            else:
                best = min(costs[0:k])
                costs.remove(best)
                costs.append(best)
                p -= 1
                m -= best
    print(plays)
        