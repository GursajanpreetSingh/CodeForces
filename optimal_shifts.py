t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    start = s.find("1")
    max_zeroes = 0
    zeroes = 0
    for _ in range(n):
        i = start % n
        if s[i] == '0':
            zeroes += 1
            max_zeroes = max(zeroes,max_zeroes)
        else:
            zeroes = 0
        start += 1
    print(max_zeroes)
