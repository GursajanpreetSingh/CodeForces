t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n<=3:
        print("NO")
        continue
    else:
        possible = False
        for i in range(n-1):
            if(s[i:i+2] in s[i+2:]):
                possible=True
                break
        if(possible):
            print("YES")
        else:
            print("NO")
    