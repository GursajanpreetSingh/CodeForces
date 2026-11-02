n = int(input())
count = 1
for i in range(2,n//2 + 1):
    if(n-i)%i == 0:
        count += 1
print(count)