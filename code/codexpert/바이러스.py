# def pprint():
#     for i in range(cnt_com):
#         print(*matrix[i])

def solution(now):
    global cnt
    for i in range(cnt_com):
        if matrix[now][i] and not chk[i]:
            cnt += 1
            chk[i] = 1
            solution(i)


cnt_com = int(input())
cnt_edge = int(input())
edges = [list(map(lambda x: int(x)-1, input().split())) for _ in range(cnt_edge)]
matrix = [[0 for _ in range(cnt_com)] for _ in range(cnt_com)]

for i in range(cnt_edge):
    matrix[edges[i][0]][edges[i][1]] = 1
    matrix[edges[i][1]][edges[i][0]] = 1

cnt = 0
chk = [0]*cnt_com
chk[0]=1
solution(0)
# pprint()
print(cnt)