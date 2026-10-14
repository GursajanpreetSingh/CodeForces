t = int(input())
for _ in range(t):
    a,b,n = map(int,input().split())
    n_arr = list(map(int,input().split()))
    time = b
    for i in range(n):
        time += min(n_arr[i],a-1)
    print(time)