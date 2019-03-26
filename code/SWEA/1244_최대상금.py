import time

def completly(cards, times):
    global answer, maxN
    if int(''.join(cards)) == maxN:
        times = 0
        if times%2:
            cards[-1], cards[-2] = cards[-2], cards[-1]
            answer.update([int(''.join(cards))])
            return
        else:
            answer.update([int(''.join(cards))])
            return
    if not times:
        answer.update([int(''.join(cards))])
        maxN = max(maxN, int(''.join(cards)))
        return
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i] <= cards[j]:
                cards[i], cards[j] = cards[j], cards[i]
                if int(''.join(cards)) not in answer:
                    completly(cards, times-1)
                cards[i], cards[j] = cards[j], cards[i]

start_time = time.time()
T = int(input())
for tc in range(T):
    cards, times = input().split()
    cards, times = list(cards), int(times)
    answer = set()
    maxN = cards[:]
    maxN.sort(reverse=True)
    maxN =int(''.join(maxN))
    completly(cards, times)
    # print(answer)
    print(max(answer))
    # print(''.join(answer))

print(time.time-start_time)