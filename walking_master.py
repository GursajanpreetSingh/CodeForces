t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    y_steps = d-b
    x_steps = (a+y_steps) - c
    if x_steps >= 0 and y_steps >=0:
        print(x_steps+y_steps)
    else:
        print(-1)
