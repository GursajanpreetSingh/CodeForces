t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    m_arr = list(map(int,input().split()))
    k_arr = list(map(int,input().split()))
    s = []
    if n-k > 1:
        s = '0' * m
    elif n == k:
        s = '1' * m
    else:
        missing_num = n*(n+1)//2 - sum(k_arr)
        for i in m_arr:
            if i != missing_num:
                s.append('0')
            else:
                s.append('1')
    print(''.join(s))


