n = int(input())
magnets = []
for _ in range(n):
    x  = int(input())
    magnets.append(x)

groups = 1
for i in range(1,n):
    if(magnets[i]!=magnets[i-1]):
        groups += 1
print(groups)