s = input()
k = int(input())
len_s = len(s)
unique_s = len(set(s))
if len_s >= k:
    print(max(0,k-unique_s))
else:
    print("impossible")