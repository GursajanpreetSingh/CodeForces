t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    unique=set(arr)

    if(len(unique)==1):
        print("Yes")
    elif(len(unique)==2):
        unique_count = []
        for el in unique:
            unique_count.append(arr.count(el))
        if(abs(unique_count[0]-unique_count[1]) == 0 or abs(unique_count[0]-unique_count[1]) == 1):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
