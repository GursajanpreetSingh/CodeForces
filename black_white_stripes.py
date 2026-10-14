t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    l = 0
    r = k-1
    count_w = s[l:r+1].count('W')
    min_w = count_w
    l+= 1
    r += 1
    while(r<n):
        if s[l-1] == 'W':
            count_w -= 1
        if s[r] == 'W':
            count_w += 1
        min_w = min(min_w,count_w)
        l+= 1
        r += 1
    print(min_w)

