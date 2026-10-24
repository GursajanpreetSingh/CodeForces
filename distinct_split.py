t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    seen1 = set()
    seen2 = set()
    done = True
    for el in s:
        if el not in seen1 and done:
            seen1.add(el)
        else:
            done = False
            seen2.add(el)

    print(len(seen1)+len(seen2))
