t = int(input())
for _ in range(t):
    s = input()
    arr = list(s)
    count = 0
    if arr[0] == 'u':
        count += 1
        arr[0] = 's'
    if arr[-1] == 'u':
        count += 1
        arr[-1] = 's'
    for i in range(1,len(arr)):
        if arr[i] == 'u' and arr[i+1] == 'u':
            count += 1
            arr[i+1]='s'
    
    print(count)