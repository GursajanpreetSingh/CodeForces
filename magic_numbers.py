s = input()
is_magic = True
if s.count('1') + s.count('4') == len(s):
    if s[0] != '1':
        is_magic = False
    if s.count('444') > 0:
        is_magic = False
else:
    is_magic = False
if is_magic:
    print("YES")
else:
    print("NO")
