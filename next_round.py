n,k = map(int,input().split())
arr = list(map(int,input().split()))
adv = 0
for i in range(n):
    if arr[i]>=arr[k-1] and arr[i]>0:
        adv += 1
    elif arr[i]<arr[k-1]:
        break
print(adv)