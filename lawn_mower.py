t = int(input())
for _ in range(t):
    n,w = map(int,input().split())
    a = n//w
    b = n%w
    fences_removed = a*(w-1) + b
    print(fences_removed)