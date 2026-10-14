t = int(input())
for _ in range(t):
    l,a,b = map(int,input().split())
    max_prize = a
    for i in range(l):
        curr_prize = (a + i*b)%l
        if curr_prize > max_prize:
            max_prize = curr_prize
    
    print(max_prize)


# Method 2

# import math

# t = int(input())
# for _ in range(t):
#     l, a, b = map(int, input().split())
    
#     # 1. Find the GCD of the step size and the wheel size
#     g = math.gcd(b, l)
    
#     # 2. Find the offset based on your starting position
#     r = a % g
    
#     # 3. Calculate and print the mathematical maximum
#     print(l - g + r)