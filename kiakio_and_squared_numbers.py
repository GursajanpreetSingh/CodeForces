def sum_of_squared(x):
    return(sum(int(d)**2 for d in str(x)))

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    count = {}

    for x in a:
        for _ in range(20):
            x = sum_of_squared(x)

        count[x] = count.get(x,0)+1

    ans = 0

    for c in count.values():
        ans += c*(c-1)//2

    print(ans)
