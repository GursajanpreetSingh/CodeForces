s = input()
ans = ""
i=0
while(i<len(s)-1):
    if(s[i]=='-' and s[i+1]=='.'):
        ans += '1'
        i += 2
    elif(s[i]=='-' and s[i+1]=='-'):
        ans += '2'
        i+= 2
    else:
        ans += '0'
        i+= 1
if(i==len(s)-1):
    ans += '0'
print(ans)
