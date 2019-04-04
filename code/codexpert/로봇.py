def solution(start, end):
    queue = [start]
    while queue:
        i,j,d = queue.pop(0)
        # 1칸 2칸 3칸가는 경우
        for i in range(3):
        # 방향전환 하는 경우



direction = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
# orders = (())
m,n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))