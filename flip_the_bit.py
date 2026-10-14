t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    k_arr = int(input())
    p_index = k_arr - 1
    l_ops = 0
    for left in range(p_index-1,-1,-1):
        if arr[left] != arr[left+1]:
            l_ops += 1
    r_ops = 0
    for right in range(p_index+1,n):
        if arr[right] != arr[right-1]:
            r_ops += 1
    

    total_ops = max(l_ops,r_ops)  
    if total_ops % 2 == 0:
        print(total_ops)
    else:
        print(total_ops+1)

