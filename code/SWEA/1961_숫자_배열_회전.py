T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    # 출력물을 담을 테이블 만들기
    table = [[] for _ in range(n)]
    # 90도 돌리기
    for j in range(n):
        ans = ''
        for i in range(n-1, -1, -1):
            ans += matrix[i][j]
        table[j] += [ans]
    
    # 180도 돌리기
    for i in range(n-1, -1, -1):
        ans = ''
        for j in range(n-1, -1, -1):
            ans += matrix[i][j]
        table[n-1-i] += [ans]
    
    # 270도 돌리기
    for j in range(n-1, -1, -1):
        ans = ''
        for i in range(n):
            ans += matrix[i][j]
        table[n-1-j] += [ans]
    
    print(f'#{tc}')
    for i in range(n):
        print(*table[i])