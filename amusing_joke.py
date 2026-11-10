s1 = input()
s2 = input()
s3 = input()

if(sorted(list(s1)+list(s2)) == sorted(list(s3))):
    print("YES")
else:
    print("NO")