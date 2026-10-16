n = int(input())
cards = list(map(int,input().split()))
s_score = 0
d_score = 0
left=0
right=n-1
while(left<right):
    if(cards[left]>cards[right]):
        s_score += cards[left]
        left += 1
    else:
        s_score += cards[right]
        right -= 1

    if(cards[left]>cards[right]):
        d_score += cards[left]
        left += 1
    else:
        d_score += cards[right]
        right -= 1
if(left==right):
    s_score += cards[left]
print(f"{s_score} {d_score}")