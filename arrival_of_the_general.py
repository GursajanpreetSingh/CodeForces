n = int(input())
arr  = list(map(int,input().split()))
max_idx = arr.index(max(arr))
min_idx = n - 1 - arr[::-1].index(min(arr))

ans = max_idx + (n-1-min_idx)

if max_idx > min_idx:
    ans -= 1

print(ans)