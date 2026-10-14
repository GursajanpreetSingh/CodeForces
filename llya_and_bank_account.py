n = int(input())

if n<0:
    n=abs(n)
    last_removed = -(n // 10)
    second_last_removed = -(int(n / 100) * 10 + n %10)
    print(max(last_removed,second_last_removed))
else:
    print(n)