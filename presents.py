n = int(input())
arr = list(map(int,input().split()))

ans = []
for i in range(1,n+1):
    ans.append(arr.index(i)+1)

print(*ans)