t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ones = arr.count(1)
    minus_ones = n - ones
    ops = 0
    if ones < minus_ones:
         ops = (n+1)//2 - ones
    if (minus_ones - ops) %2 == 0:
         print(ops)
    else:
         print(ops+1)