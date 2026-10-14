n = int(input())
s = "I hate "
for i in range(n-1):
    s += "that "
    if i %2 == 0:
        s += "I love "
    else:
        s += "I hate "
s += "it"
print(s)
