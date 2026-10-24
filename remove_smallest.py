t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    if n==1:
        print("YES")
    else:
        arr.sort()
        is_possible = True
        for i in range(n-1): 
            if(abs(arr[i]-arr[i+1])> 1):
                is_possible = False
                break
        print("YES" if is_possible else "No")


    
