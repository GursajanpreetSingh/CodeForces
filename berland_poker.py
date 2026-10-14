t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    cards_per_player = int(n/k)
    max_jokers_from_winner = min(cards_per_player,m)
    remaining_jokers = m - max_jokers_from_winner
    max_jokers_from_runner_up = -(-remaining_jokers//(k-1))
    points = max_jokers_from_winner - max_jokers_from_runner_up
    print(points)
