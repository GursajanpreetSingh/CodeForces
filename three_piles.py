t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    score = max(abs(a-b),abs(a+c-b))
    print(score)
