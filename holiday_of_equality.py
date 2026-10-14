n = int(input())
arr = list(map(int,input().split()))
highest = max(arr)
S = 0
for i in arr:
    S += highest-i
print(S)