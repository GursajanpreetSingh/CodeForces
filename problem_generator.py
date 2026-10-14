t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    s = input()
    usable_problems = 0
    for char in 'ABCDEFG':
        usable_problems += min(s.count(char),m)
    result = 7*m - usable_problems
    print(result)