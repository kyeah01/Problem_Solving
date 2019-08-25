def solution(numbers, target):
    def DFS(now, i):
        nonlocal answer
        if i >= len(numbers):
            if now == target:
                answer += 1
            return 
        DFS(now+numbers[i], i+1)
        DFS(now-numbers[i], i+1)
    answer = 0
    DFS(0, 0)
    return answer