s = input()
s = s.split("WUB")
for i in range(s.count('')):
    s.remove('')
s = " ".join(s)
print(s)
