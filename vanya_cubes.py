n = int(input())
i = 1
npl = 0
while(True):
    if n >= npl + i:
        n -= npl+i
        npl += i
        i += 1
    else:
        break
print(i-1)