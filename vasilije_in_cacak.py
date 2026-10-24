t = int(input())
for _ in range(t):
    n,k,x = map(int,input().split())
    least = int(k*(k+1)/2)
    atmost = n*k - least + k
        
    if x in range(least,atmost+1):
        print("YES")
    else:
        print("NO")
    