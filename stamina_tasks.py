t = int(input())
for _ in range(t):
    n = int(input())
    tasks = []
    for i in range(n):
        c,p = list(map(int,input().split()))
        tasks.append([c,p])
    points = 0
    for i in range(n-1,-1,-1):
        c=tasks[i][0]
        p = tasks[i][1]

        points_if_skipped = points

        points_if_done = c + points*(1- p/100)

        if points_if_done>points_if_skipped:
            points=points_if_done
    print(points)