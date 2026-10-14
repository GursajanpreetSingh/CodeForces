t = int(input())
for _ in range(t):
    arr = []
    for i in range(8):
        s = input()
        arr.append(s)

    for i in range(8):
        new_s = arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i] + arr[5][i] +arr[6][i] + arr[7][i]
        if len(new_s.strip(".")) > 0:
            print(new_s.strip("."))
            break