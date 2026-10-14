n,l = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
differences = []
differences.append(arr[0]-0)
differences.append(l-arr[n-1])
for i in range(n-1):
    differences.append((arr[i+1]-arr[i])/2)
print(f"{max(differences):.10f}")
