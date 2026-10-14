n = abs(int(input()))
jumps=0
p = 0

while p < n or(p-n)%2 !=0:
    jumps += 1
    p += jumps

print(jumps)

    