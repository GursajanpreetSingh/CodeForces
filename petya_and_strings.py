s1 = input().lower()
s2 = input().lower()
ans = 0
for i in range(len(s1)):
    if s1[i] < s2[i]:
        ans = -1
        break
    elif s1[i] > s2[i]:
        ans = 1
        break
print(ans)