t = int(input())
for _ in range(t):
    n = int(input())
    if(n==1 or n==2):
        print(0)
    else:
        if(n%2==0):
            print(n//2 - 1)
        else:
            print(n//2)