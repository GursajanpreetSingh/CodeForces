t = int(input())
for _ in range(t):
    n = int(input())
    counter = 0
    if(n%6==3):
         counter +=1
         n *= 2
    while(n%6==0):
        n = n//6
        counter += 1
        if(n%6==3):
            counter +=1
            n *= 2
    if(n==1):
        print(counter)
    elif(n==3):
        counter += 2
        print(counter)
    elif(n==9):
        counter += 4
        print(counter)
    else:
        counter = -1
        print(counter)
    
        