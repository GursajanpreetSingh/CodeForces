n = int(input())
steps = n // 5
if n%5 > 0:
    steps += 1
print(steps)