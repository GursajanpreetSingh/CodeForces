n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
bob_money = 0
for i in range(m):
    if arr[i] < 0:
        bob_money += arr[i]
    else:
        break
print(-1 * bob_money)

