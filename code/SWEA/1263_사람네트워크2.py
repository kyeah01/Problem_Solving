def solution(n, desserts):
    direction = [(-1,1), (1,1),(1,-1),(-1,-1)]
    
    i,j = 1,0
    # 대각선을 만들 수 있는 점들은 i가 1이상, n-2이하일 경우, j는 0이상, n-3이하일 경우.
    for i in range(1, n-1):
        for j in range(n-2):
            
    # if 0<i<n-1 and 0<=j<n-2:
        # 이면 순회를 시작할 수 있다.
        # 맨처음 -1,1의 과정, 직진을 몇번 할 것인지(1번부터~ 할수있는만큼:늘 달라지기때문에!)
        #  (직진할수있는 횟수만큼 따로 돌아야 함. i가 k면 k번 갈 수 있음.)
        # 마찬가지로 가려고 하는 만큼 가고, 간 길이 저장한다음에
        #  (마찬가지로 j가 k면 n-1-k번 갈 수 있음.)
        # 그 뒤로 방향전환한 뒤로는 그냥 갔던만큼 가고, 갔던만큼 가는 코스를 진행해야함.
    def set_garo(k):
        return [k for i in range(1,k)]

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    desserts = [list(map(int, input().split())) for _ in range(n)]
