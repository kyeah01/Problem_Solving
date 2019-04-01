# 일차원인 최장증가수열 구하기
# def sequence(n):
#     seq = []
#     for i in range(n):
#         if seq:
#             if seq[-1] <= sousages[i]:
#                 seq += [sousages[i]]
#             else:
#                 while seq[-1] > sousages[i]:
#                     seq.pop()
#                 seq += [sousages[i]]
#         else:
#             seq += [sousages[i]]
#     print(seq)


# 2차원인 최장증가수열 구하기
def sequence(n):
    seq = []
    result = []
    for i in range(n):
        if seq:
            if seq[-1][0] > sousages[i][0] or seq[-1][1] > sousages[i][1]:
                while seq and (seq[-1][0] > sousages[i][0] or seq[-1][1] > sousages[i][1]):
                    seq.pop()
                    result.pop()
        seq += [sousages[i]]
        result += [i]
        
        # if seq:
        #     if seq[-1][0] <= sousages[i][0] and seq[-1][1] <= sousages[i][1]:
        #         seq += [sousages[i]]
        #     else:
        #         seq.pop() sousages[i]랑 둘이 비교해서 더 작은 걸 넣자.
        #         # while seq and (seq[-1][0] > sousages[i][0] or seq[-1][1] > sousages[i][1]):
        #         #     seq.pop()
        #         # seq += [sousages[i]]
        #         pass
        # else:
        #     seq += [sousages[i]]
    # print(seq)
    return seq
    # return result


def solution(n):
    global sousages
    x = n
    save = sousages[:]
    time1, time2 = 0,0
    while sousages:
        time1 += 1
        sousages.sort()
        for s in sequence(x):
            # print(s)
            # print(sousages)
            sousages.remove(s)
            x -= 1
    sousages = save
    while sousages:
        time2 += 1
        sousages.sort(key=lambda x:x[1])
        for s in sequence(n):
            sousages.remove(s)
            n -= 1
    return min(time1, time2)

n = int(input())
sousages = list(map(int,input().split()))
sousages = [(sousages[i], sousages[i+1]) for i in range(0,n*2,2)]
print(solution(n)+1)