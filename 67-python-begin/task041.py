teams = {}
for i in range(int(input())):
    match = input().split(';')
    match[1] = int(match[1])
    match[3] = int(match[3])
    teams.setdefault(match[0], [0, 0, 0, 0, 0]);
    teams.setdefault(match[2], [0, 0, 0, 0, 0]);
    teams[match[0]][0] += 1
    teams[match[2]][0] += 1
    if match[1] > match[3]: # победа первой команды
        teams[match[0]][1] += 1
        teams[match[0]][4] += 3
        teams[match[2]][3] += 1
    elif match[1] < match[3]: # победа второй команды
        teams[match[2]][1] += 1
        teams[match[2]][4] += 3
        teams[match[0]][3] += 1
    else: # ничья
        teams[match[0]][2] += 1
        teams[match[0]][4] += 1
        teams[match[2]][2] += 1
        teams[match[2]][4] += 1
for team, score in teams.items():
    print('{}:{}'.format(team, ' '.join(map(str, score))))