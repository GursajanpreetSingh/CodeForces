n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr_ceil = []
arr_ceil.append(-(arr[0]//-m))
max = arr_ceil[0]
max_idx = 1
for i in range(1,n):
    arr_ceil.append(-(arr[i]//-m))
    if arr_ceil[i] >= max:
        max = arr_ceil[i]
        max_idx = i+1
print(max_idx)