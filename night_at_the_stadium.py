s = input()
ans = 0
alphabets = "abcdefghijklmnopqrstuvwxyz"
current = "a"
for i in s:
    curr_pos = alphabets.find(current)
    i_pos = alphabets.find(i)
    diff = abs(curr_pos-i_pos)

    ans += min(diff,26-diff)
    current = i

print(ans)