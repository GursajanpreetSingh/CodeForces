t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a == b:
        ops = 0
    elif a % b == 0 or b % a == 0:
        ops = 1
    else:
        ops = 2
    print(ops)