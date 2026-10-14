n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x_y = set(x[1:]+y[1:])
if len(x_y)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')