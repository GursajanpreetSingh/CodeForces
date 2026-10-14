t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))

    low = 1
    high = max(arr) + x

    while low <= high:
        mid = (low+high)//2

        water = 0

        for a in arr:
            if a < mid:
                water += mid-a

        if water <= x:
            low = mid +1
        else:
            high = mid -1

    print(high)