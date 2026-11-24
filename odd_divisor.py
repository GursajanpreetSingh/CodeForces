t= int(input())
for _ in range(t):
    n = int(input())
    exists = False
    if(n%2 !=0 ):
        exists = True
    elif(n==2):
        exists = False
    else:
        i = n/2
        while(i>=3):
            i = i/2
            if(i%2!=0):
                exists = True
                break
    print("YES" if exists else "NO")
        