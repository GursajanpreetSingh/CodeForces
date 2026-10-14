t = int(input())
for _ in range(t):
    k = int(input())
    num = 1
    while(k>1):
        num += 1
        if(num%3!=0 and num%10!=3):
            k -= 1
    print(num)