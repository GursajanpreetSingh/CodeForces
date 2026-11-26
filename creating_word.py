t = int(input())
for _ in range(t):
    a,b = input().split()
    newa = b[0]+a[1]+a[2]
    newb = a[0]+b[1]+b[2]
    print(newa,newb)