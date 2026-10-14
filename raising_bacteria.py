n = int(input())
bacteria_added = 0
while n > 0:
    if n % 2 != 0:
        bacteria_added += 1
    n = n//2
print(bacteria_added)