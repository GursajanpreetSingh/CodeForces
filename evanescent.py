t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    original = 1

    for i in range(1,n):
        if s[i]!=s[i-1]:
            original += 1

    ans = original
    for i in range(1,n-1):
        new_length = (original - (s[i]!=s[i-1])- (s[i]!=s[i+1])+ (s[i-1]!=s[i+1]))

        ans = min(ans,new_length)

    print(ans)