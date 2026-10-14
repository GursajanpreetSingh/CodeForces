n = int(input())
arr = list(map(int,input().split()))
maximum = 1
maxi = 1
for i in range(1,n):
    if arr[i]>=arr[i-1]:
        maxi+=1
    else:
        maxi = 1
    maximum = max(maxi,maximum)
print(maximum)
