def judging(cards):
    
    def judgement(arr):
        arr.sort()
        set_arr = sorted(list(set(arr)))
        for i in range(len(set_arr)-2):
            if set_arr[i]+2 == set_arr[i+1]+1 == set_arr[i+2]:
                return True
        for i in range(len(arr)-2):
            if arr[i] == arr[i+1] == arr[i+2]:
                return True
        return False
    
    player_1, player_2 = [], []
    for i in range(0, 12, 2):
        player_1 += [cards[i]]
        if i >=3:
            if judgement(player_1):
                return 1
        player_2 += [cards[i+1]]
        if i >=3:
            if judgement(player_2):
                return 2
    return 0

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    print('#{}'.format(tc), judging(cards))