t = int(input())
for _ in range(t):
    x,k = map(int,input().split())
    # n = int(str(x) * k)
    is_prime = True
    
    if k == 1:
        if x < 2:
            is_prime = False
        elif x == 2:
            is_prime = True
        elif x % 2 == 0:
            is_prime = False
        else:
            limit = int(x**0.5) + 1
            for i in range(3,limit,2):
                if x % i == 0:
                    is_prime = False
                    break
    elif x == 1 and k == 2:
        is_prime = True
    else:
        is_prime = False
    if is_prime:
        print("YES")
    else:
        print("NO")