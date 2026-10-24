n = int(input())
arr = [2]*(n//2 - 1)
if n%2 == 0:
    arr.append(2)
    ans = len(arr)
else:
    arr.append(3)
    ans = len(arr)
print(ans)
print(*arr)
