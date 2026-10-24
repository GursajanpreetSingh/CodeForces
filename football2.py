n = int(input())
goals = []
for _ in range(n):
    x = input()
    goals.append(x)

teamA = goals[0]
teamAGoals = 0
teamBGoals = 0
for goal in goals:
    if goal == teamA:
        teamAGoals += 1
    else:
        teamB = goal
        teamBGoals += 1

print(teamA if teamAGoals>teamBGoals else teamB)