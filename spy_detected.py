t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    if(arr[0]==arr[1]):
        not_spy = arr[0]
    else:
        if(arr[0]==arr[2]):
            not_spy = arr[0]
        else:
            not_spy = arr[1]

    for i in range(n):
        if(arr[i]!=not_spy):
            print(i+1)
            break