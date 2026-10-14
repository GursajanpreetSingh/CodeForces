s = input()
seen = set()
for i in s:
    if i not in seen:
        seen.add(i)

if(len(seen)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")