t = int(input())
for _ in range(t):
    n = int(input())
    extra_candies = 0
    if n%3 > 0:
        extra_candies = 3 - n%3
    print(extra_candies)