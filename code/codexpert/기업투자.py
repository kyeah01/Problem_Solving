def comb(k, now):
    global maxN
    if k == company:
        if plan[k-1] == budget:
            print(plan)
            for j in range(company-1, 0, -1):
                plan[j] -= plan[j-1]
            print('plan', plan)
            total = 0
            # print(investment)
            for j in range(company):
                if plan[j]:
                    # print(investment[plan[j]-1], investment[plan[j]-1][j+1])
                    total += investment[plan[j]-1][j+1]
            maxN = max(maxN, total)
        return
    for i in range(now,budget+1):
        plan[k] = i
        comb(k+1, i)



budget, company = map(int, input().split())
investment = [list(map(int,input().split())) for _ in range(budget)]
plan = [0]*company
maxN = 0
comb(0,0)
print(maxN)