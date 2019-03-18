k = int(input())
melon = [list(map(int, input().split())) for _ in range(6)]
field = {i:[] for i in range(1,5)}
for m in range(6):
    field[melon[m][0]] += [melon[m][1]]
if len(field[1]) == 2:
    long_garo = 