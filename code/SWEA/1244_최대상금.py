T = int(input())
for tc in range(T):
    cards, times = input().split()
    cards, times = list(cards), int(times)
    i = 0
    while times :
        max_index = -cards[i:][::-1].index(max(cards[i:]))-1
        if len(cards)+max_index != i:
            cards[max_index], cards[i] = cards[i], cards[max_index]
            i += 1
            times -= 1
        else:
            i += 1
        if len(cards[i:]) < 2:
            break
    while times:
        cards[-1], cards[-2] = cards[-2], cards[-1]
        times -= 1
    print(''.join(cards))