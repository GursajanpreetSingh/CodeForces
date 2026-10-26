s = input()
lowercase = 0
uppercase = 0
for el in s:
    if el.islower():
        lowercase += 1
    else:
        uppercase += 1
if(lowercase>=uppercase):
    print(s.lower())
else:
    print(s.upper())