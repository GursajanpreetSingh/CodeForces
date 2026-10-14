t = int(input())
for _ in range(t):
    n = int(input())
    min = -1
    max = -1
    if n<=6:
        if n == 4 or n ==6:
            min = 1
            max = 1
    else:
        if n % 6 == 0:
            min = n//6
        elif n % 6 == 4 or n % 6 == 2:
            min = n//6 + 1
        if n % 4 == 0 or n % 4 == 2:
            max = n//4
    
    if min == -1 and max == -1:
        print(-1)
    elif min == -1 and max != -1:
        print(max,max)
    elif min != -1 and max == -1:
        print(min,min)
    else:
        print(min,max)
        
        
