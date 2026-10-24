t = int(input())
for _ in range(t):
    n = int(input())
    excluded_digits = list(map(int,input().split()))
    numOfSequences = 3 * (10-n) * (9-n)
    print(numOfSequences)
    