n = int(input())
result = 0
for _ in range(n):
    x = list(map(int,input().split()))
    if x.count(1)>1:
        result += 1
print(result)