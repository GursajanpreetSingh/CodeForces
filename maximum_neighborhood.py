t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        max_cost = 1
    elif n==2:
        max_cost = 9
    elif n==3 or n ==4:
        el = n*n -1
        max_cost = 4*el - n
    else:
        el = n*(n-1)-1
        max_cost = 5*el
    print(max_cost)