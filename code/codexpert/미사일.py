def solution(N):
    def damage(warship, i,j,d,rgn):
        for i in range(N):
            if abs(i-warship[i][0])+abs(j-warship[i][1]) <= rgn:
                warship[i][2] -= d
        return warship
    
    def setting(k, warship):
        nonlocal maxN
        if k == missile[0]:
            cnt = 0
            for i in range(N):
                if warship[i][2] <= 0:
                    cnt += 1
            maxN = max(maxN, cnt)
            return
        for i in range(N):
            war = [warship[i][:] for i in range(N)]
            war = damage(war, warship[i][0], warship[i][1], missile[1], missile[2])
            setting(k+1, war)
    
    maxN = 0
    war = [warship[i][:] for i in range(N)]
    setting(0, war)
    print(maxN)


N = int(input())
warship = [list(map(int, input().split())) for _ in range(N)]
missile = list(map(int, input().split()))
solution(N)