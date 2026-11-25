n = int(input())
count = 0
for el in str(n):
    if el=='4' or el=='7':
        count += 1
nearly_lucky=True
for el in str(count):
    if el != '4' and el!='7':
        nearly_lucky = False
        break
print("YES" if nearly_lucky else "NO")
