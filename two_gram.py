n = int(input())
s = input()
lis = []
for i in range(n-1):
    lis.append(s[i]+s[i+1])
result = max(set(lis), key=lis.count)
print(result)