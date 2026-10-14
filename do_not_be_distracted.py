t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    tasks_done = set()
    flag = True
    for i in range(1,n):
        if s[i] in tasks_done:
            flag = False
            break
        if s[i] != s[i-1]:
            tasks_done.add(s[i-1])
    if flag:
        print("YES")
    else:
        print("NO")