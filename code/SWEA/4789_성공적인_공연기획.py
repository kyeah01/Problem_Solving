T = int(input())

for tc in range(1, T+1):
    crowd = list(map(int, input()))
    i = cnt = num = 0
    for i in range(len(crowd)):
        num -= 1
        if crowd[i]:
            num += crowd[i]
        else:
            if num<=0:
                cnt += 1
            else:
                num -= 1
    print(cnt)