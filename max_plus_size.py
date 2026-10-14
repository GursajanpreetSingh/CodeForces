t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxi = max(arr)
    if n % 2 == 0:
        score = maxi + int(n/2)
    else:
        for i in range(n):
            if arr[i] == maxi and i % 2 == 0:
                score = maxi + int(n//2) + 1
                break
            else:
                score = maxi + int(n//2)
    print(score)