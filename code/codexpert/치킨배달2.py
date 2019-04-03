def solution():
    def driver(x,y):
        nonlocal result
        temp = []
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 1:
                    temp += [abs(x-i)+abs(y-j)]
        result += [temp]
        
    def chicken():
        nonlocal house
        cnt = 0
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 2:
                    cnt += 1
                    driver(i,j)
                if maps[i][j] == 1:
                    house += 1
        return cnt
    
    def choose(k, time):
        nonlocal fin, minN
        if k == m:
            if sum(choice) == m:
                total = 0
                for i in range(cnt):
                    if choice[i]:
                        minn = 0xffffff
                        for j in range(house):
                            minn = min(minn, result[i][j])
                        total += minn
                minN = min(minN, total)
            return
        for i in range(k, cnt):
            choice[i] = 1
            choose(k+1, time+1)
            choice[i] = 0        

    result = []
    house = 0
    cnt = chicken()
    choice = [0]*cnt
    fin = []
    minN = 0xffffff
    choose(0, 0)
    print(minN)

n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
solution()