def check(numbers, colors):
    cnt = 0
    for i in range(9):
        for j in range(i+1, 9):
            if numbers[i]+1 == numbers[j] or numbers[i] == numbers[j]:
                for k in range(j+1, 9):
                    if numbers[i]+2 == numbers[j]+1 == numbers[k]:
                        if len({colors[i], colors[j], colors[k]}) == 1:
                            cnt += 1
                    elif numbers[i] == numbers[j] == numbers[k]:
                        if len({colors[i], colors[j], colors[k]}) == 1:
                            cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    numbers, colors = [input() for _ in range(2)]
    numbers = list(map(int, numbers))
    print(check(numbers, colors))
