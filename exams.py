d,SumTime = map(int,input().split())
min_time = []
max_time = []
for i in range(d):
    day = list(map(int,input().split()))
    min_time.append(day[0])
    max_time.append(day[1])

total_min_time = sum(min_time)
total_max_time = sum(max_time)

if total_min_time <= SumTime <= total_max_time:
    print("YES")
    while(total_min_time < SumTime):
        for j in range(d):
            if total_min_time < SumTime and min_time[j] < max_time[j]:
                min_time[j] += 1
                total_min_time += 1
    print(*min_time)
else:
    print("NO")