n = int(input())
arr = list(map(int,input().split()))
maxChocolates = arr[n-1]
for i in range(n-2,-1,-1):
    if (arr[i] < arr[i+1]):
        maxChocolates += arr[i]
    else:
        if (arr[i+1]-1) == 0:
            break
        else:
            maxChocolates += (arr[i+1]-1)
            arr[i] = arr[i+1]-1
    
print(maxChocolates)