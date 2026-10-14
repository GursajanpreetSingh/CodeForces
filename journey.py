t = int(input())
for _ in range(t):
    n,a,b,c = map(int,input().split())
    days = [a,b,c]
    all_three_days = n // (sum(days))
    total_days = all_three_days * 3
    remaining_dist = n - sum(days) * all_three_days
    for i in days:
        if remaining_dist > 0:
            total_days += 1
            remaining_dist -= i
    print(total_days)
