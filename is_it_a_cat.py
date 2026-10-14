t = int(input())
for _ in range(t):
    n = int(input())
    s = input().lower()
    sound = ['m','e','o','w']
    is_meow = False
    if "m" in s and 'e' in s and 'o' in s and 'w' in s:
        for i in sound:
            s = s.lstrip(i)
    if len(s) == 0:
        print("YES")
    else:
        print("NO")

    