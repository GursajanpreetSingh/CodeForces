n = int(input())
enters = []
exits = []
for _ in range(n):
    a,b = map(int,input().split())
    enters.append(a)
    exits.append(b)

min_capacity = 0
curr_capacity = 0
for i in range(n):
    curr_capacity -= enters[i]
    curr_capacity += exits[i]

    min_capacity = max(min_capacity,curr_capacity)

print(min_capacity)

