n = int(input())
scores = []
for _ in range(n):
    m_c = list(map(int,input().split()))
    scores.append(m_c)
m_score = 0
c_score = 0
for i in range(n):
    if scores[i][0] > scores[i][1]:
        m_score += 1
    elif scores[i][0] < scores[i][1]:
        c_score += 1
if m_score > c_score:
    print("Mishka")
elif c_score > m_score:
    print("Chris")
else:
    print("Friendship is magic!^^")