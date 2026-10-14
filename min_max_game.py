t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if arr.count(1) >= arr.count(0):
        print("Bessie")
    else:
        print("Elsie")

