def solution():
    def chicken():
        shop = []
        house = []
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 2:
                    shop += [(i,j)]
                if maps[i][j] == 1:
                    house += [(i,j)]
        return shop, house
    
    def driver():
        # result = []
        # for i in range(len(shop)):
        #     temp = []
        #     for j in range(len(house)):
        #         temp += [abs(shop[i][0]-house[j][0]) + abs(shop[i][1]-house[j][1])]
        #     result += [temp]
        # return result
        return [[abs(shop[i][0]-house[j][0]) + abs(shop[i][1]-house[j][1]) for j in range(len(house))] for i in range(len(shop))]
    
    def choose(k, time):
        nonlocal fin, minN
        if time == m:
            # print(choice)
            total = 0
            for j in range(len(house)):
                # print(result[i])
                minn = 20*20
                for i in range(len(shop)):
                    if choice[i]:
                        minn = min(minn, result[i][j])
                total += minn
            minN = min(minN, total)
            return
        if k == len(shop):
            return
        choice[k] = 1
        choose(k+1, time+1)
        choice[k] = 0
        choose(k+1, time)


    result = []
    shop, house = chicken()
    choice = [0]*len(shop)
    fin = []
    result = driver()
    minN = 0xffffff
    # print(minN)
    choose(0, 0)
    print(minN)

n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
solution()