t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    diff_arr = []
    ops = 0
    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        diff_arr.append(diff)
    min_diff = min(diff_arr)
    if min_diff < 0:
        ops = 0
    elif min_diff == 0:
        ops = 1
    else:
        ops = min_diff//2 + 1
    print(ops)
        
