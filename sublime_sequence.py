t = int(input())
for _ in range(t):
    x,n = map(int,input().split())
    if n % 2 == 0:
        sum = 0
    else:
        sum = x
    print(sum)
