t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    ans = ""
    for i in range(b):
        ans += alphabets[i]

    ans = ans*(n//b + 1)
    ans = ans[:n]
    print(ans)

    