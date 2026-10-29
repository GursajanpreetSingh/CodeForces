n = int(input())
s = input()
winA = 0
winD = 0
for el in s:
    if el == 'A':
        winA += 1
    else:
        winD += 1

if(winA>winD):
    print("Anton")
elif(winD>winA):
    print("Danik")
else:
    print("Friendship")
