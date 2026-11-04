t = int(input())
for _ in range(t):
    a = int(input())
    sides = 2
    while(True):
        sides += 1
        angle = (sides-2)*180 / sides

        if(angle==a):
            print("YES")
            break
        elif(angle>a):
            print("NO")
            break
        

        