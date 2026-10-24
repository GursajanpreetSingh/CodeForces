t = int(input())
for _ in range(t):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    n = int(input())
    s = input()
    largest = max(list(s))
    print(alphabets.find(largest)+1)