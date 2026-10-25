n = int(input())
s = input()
i = 0
j= 1
ans = 0
while(j<n):
    if(s[i]==s[j]):
        ans += 1
        j += 1
    else:
        j+= 1
        i = j-1

print(ans)