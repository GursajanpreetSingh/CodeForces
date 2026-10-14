t = int(input())
for _ in range(t):
    n,c = map(str,input().split())
    n = int(n)
    s = input()
    left = 0
    right = n-1
    coins = 0
    while(left<right):
        if (s[left] != s[right]):
            if(s[left]!=c ):
                coins += 1
            if(s[right]!=c):
                coins += 1
        left += 1
        right -= 1
    print(coins)
