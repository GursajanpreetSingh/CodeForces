t = int(input())
for _ in range(t):
    s = input()
    ones = s.count('1')
    flag = False
    min_zeroes = 0
    for i in range(len(s)):
        if s[i] == '1':
            flag = True
            ones -= 1
        elif flag and s[i]=='0' and ones > 0:
            min_zeroes += 1
    print(min_zeroes)

# METHOD 2
# t = int(input())

# for _ in range(t):
#     s = input()
#     print(s.strip('0').count('0'))