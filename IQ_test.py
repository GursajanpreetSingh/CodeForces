n = int(input())
arr = list(map(int,input().split()))
even = 0
odd = 0
for i in range(3):
    if arr[i] % 2== 0:
        even += 1
    else:
        odd += 1
for i in range(n):
    if even > 1 and arr[i] % 2 != 0:
        idx = i + 1
        break
    if odd > 1 and arr[i] % 2 == 0:
        idx = i + 1
        break
print(idx)
            