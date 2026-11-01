t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    p = sorted(list(input()))
    q = sorted(list(input()))
    new_p = ""
    new_q = ""
    i = 0
    j=0
    while(i<n and j<m):
        if(p[i]==q[j]):
            i+=1
            j+=1
        elif(p[i]<q[j]):
            new_p += p[i]
            i += 1
        
        else:
            new_q += q[j]
            j += 1
    while(i<n):
        new_p += p[i]
        i += 1
    while(j<m):
        new_q += q[j]
        j +=1
        
    if new_p == "isx" and len(new_q)==0:
        print("YES")
    else:
        print("NO")
