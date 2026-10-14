t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n > 10:
        print(f"{s[0]}{n-2}{s[-1]}")
    else:
        print(s)