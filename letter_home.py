t = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    pos = list(map(int,input().split()))
    result = (pos[n-1]-pos[0]) + min(abs(s-pos[0]),abs(pos[n-1]-s))
    print(result)