n = int(input())
enter = list(map(int,input().split()))
exit = list(map(int,input().split()))

fined = 0
already_left = set()
expected_idx = 0
for i in range(n):
    while enter[expected_idx] in already_left:
        expected_idx += 1
    if exit[i] == enter[expected_idx]:
        expected_idx += 1
    else:
        fined += 1
        already_left.add(exit[i])
print(fined)