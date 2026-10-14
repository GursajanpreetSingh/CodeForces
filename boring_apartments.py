t = int(input())
for _ in range(t):
    a = input()
    total_keys_pressed = 10* (int(a[0])-1)
    for i in range(len(a)):
        total_keys_pressed += i+1
    print(total_keys_pressed)
