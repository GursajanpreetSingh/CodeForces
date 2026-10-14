t = int(input())
for _ in range(t):
    n = input()
    sum1 = 0
    sum2 = 0
    for i in range(3):
        sum1 += int(n[i])
    for j in range(3,6):
        sum2 += int(n[j])

    if sum1 == sum2:
        print("YES")
    else:
        print("NO")