mapping_table = {
    (0,0,0,1,1,0,1) : 0,
    (0,0,1,1,0,0,1) : 1,
    (0,0,1,0,0,1,1) : 2,
    (0,1,1,1,1,0,1) : 3,
    (0,1,0,0,0,1,1) : 4,
    (0,1,1,0,0,0,1) : 5,
    (0,1,0,1,1,1,1) : 6,
    (0,1,1,1,0,1,1) : 7,
    (0,1,1,0,1,1,1) : 8,
    (0,0,0,1,0,1,1) : 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    answer_sheet = []
    for i in range(N):
        j = M
        while j >= 7:
            if tuple(arr[i][j-7:j]) in mapping_table.keys():
                answer_sheet += [mapping_table[tuple(arr[i][j-7:j])]]
                print(answer_sheet, j)
                j -= 7
            else:
                j -= 1
        print(answer_sheet[::-1])
        if len(answer_sheet) > 7:
            break

    fir = sum(answer_sheet[::-1][i] for i in range(8) if not i%2)*3
    sec = sum(answer_sheet[::-1][i] for i in range(8) if i%2)
    if (fir+sec)%10:
        print(0)
    else:
        print(sum(answer_sheet))