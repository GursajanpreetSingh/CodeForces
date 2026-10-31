n = int(input())
arr  = list(map(int,input().split()))
min_idx = n
max_idx = -1
max_el = 1
min_el = 101
for i in range(n):
    if arr[i]> max_el:
        max_el = arr[i]
        max_idx = i
    if arr[i]<=min_el:
        min_el = arr[i]
        min_idx = i

ans = (max_idx-0) + (n-1-min_idx) - (max_idx > min_idx)
print(ans)