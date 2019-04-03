def solution(n, x):
    # 오른쪽에 넣거나, 왼쪽에 넣거나, 넣지않거나의 경우의 수
    def chk(k):
        nonlocal answer
        if n == k:
            # print(result)
            answer += [result[:]]
            return 
        result[k] = 2
        chk(k+1)
        result[k] = 1
        chk(k+1)
        result[k] = 0
        chk(k+1)
    
    def balance(marble):
        chk(0)
        for ans in answer:
            right = marble
            left = 0
            for i in range(n):
                if ans[i] == 2:
                    right += weights[i]
                elif ans[i]:
                    left += weights[i]
            if right == left:
                return 'Y'
        return 'N'

    final = []
    for marble in marbles:
        result = [0]*n
        answer = []
        final += [balance(marble)]
    return final

n = int(input())
weights = list(map(int, input().split()))
x = int(input())
marbles = list(map(int, input().split()))
print(*solution(n, x))