t = int(input())
for _ in range(t):
    s = input()
    ls = len(s)
    zeros = s.count('0')
    ones = ls - zeros
    lt = 0
    for i in range(ls):
        if s[i] == '0':
            if ones > 0 and s[lt]== "0":
                ones -= 1
                lt += 1
        if s[i] == '1' :
            if zeros > 0 and s[lt]== "1":
                zeros -= 1
                lt += 1

    print(ls - lt)