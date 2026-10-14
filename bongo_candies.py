t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        s = list(map(int,input().split()))
        arr.extend(s)
    unique = set(arr)
    max_occ = 1
    for j in unique:
        if arr.count(j) >= max_occ:
            max_occ = arr.count(j)
    
    if max_occ > n*n-n:
        print("NO")
    else:
        print("YES")
