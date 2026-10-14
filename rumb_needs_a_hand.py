t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    indices = []

    for i in range(n):
        if p[i]!=i+1:
            indices.append(i)

    if len(indices) == 0:
        print("YES")
        continue

    possible = True
    m = len(indices)

    for i in range(m):
        if p[indices[i]] != indices[m-i-1]+1:
            possible = False
            break

    print("YES" if possible else "NO")