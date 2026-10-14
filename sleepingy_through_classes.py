t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    not_sleep = k
    skip = 0
    flag = False
    for i in range(n):
        if s[i] == '1':
            flag = True
            not_sleep = k
        elif flag  and not_sleep>0 and s[i]=='0':
            not_sleep -= 1
        else:
            skip += 1
    print(skip)
        