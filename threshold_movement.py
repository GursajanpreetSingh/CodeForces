t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if n==1 or n%2 !=0:
        print("NO")
        continue
    else:
        possible = True
        max_k = arr[0]-1
        min_k = arr[1]+1
        
    for i in range(0,n,2):
        required_max_k = arr[i]-1
        required_min_k = arr[i+1]+1
        
        max_k = min(max_k,required_max_k)
        min_k = max(min_k,required_min_k)
        
    if min_k <= max_k:
        print("YES")
    else:
        print("NO")


