t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    total_cost = 0
    for i in range(n-1):
        total_cost += abs(arr[i]-arr[i+1])
    
    max_savings = 0
    if abs(arr[0]-arr[1]) > max_savings:
        max_savings = abs(arr[0]-arr[1])
    if abs(arr[n-2]-arr[n-1]) > max_savings:
        max_savings = abs(arr[n-2]-arr[n-1])
    for i in range(1,n-1):
        actual_cost = abs(arr[i-1]-arr[i]) + abs(arr[i]-arr[i+1])
        cost_if_removed = abs(arr[i-1]-arr[i+1])

        savings = actual_cost-cost_if_removed
        if savings > max_savings:
            max_savings = savings

    print(total_cost-max_savings)