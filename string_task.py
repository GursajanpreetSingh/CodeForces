s = input().lower()
list_s = []
vowels = [ "a", "o", "y", "e", "u", "i"]
for i in range(len(s)):
    if s[i] not in vowels:
        list_s.append(".")
        list_s.append(s[i])
    
new_s = "".join(list_s)
print(new_s)
