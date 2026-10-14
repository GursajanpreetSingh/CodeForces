t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    s = input()
    sB = s.count('B')
    q_arr = list(map(int,input().split()))
    for i in range(q):
        cost = q_arr[i]
        if sB == 0:
            counter = cost
        else:
            loc = 0
            counter = 0
            while(cost != 0):
                if s[loc] == 'A':
                    cost -= 1
                else:
                    cost = int(cost//2)
                counter += 1
                loc = (loc + 1)%(n)
        print(counter)