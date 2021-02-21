size_team = int(input())

players = [int(player) for player in input().split()]
players.sort()
players.reverse()

main_team = players[:11]
if size_team <= 22:
    reserves = players[11:]
else:
    reserves = players[11:22]

print(sum(main_team) - sum(reserves))
