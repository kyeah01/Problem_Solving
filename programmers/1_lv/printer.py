def solution(priorities, location):
    answer, current = 0, -1
    lenth = len(priorities)
    while priorities:
        work = priorities.pop(0)
        current += 1
        if current == lenth:
            current = 0
        for i in priorities:
            if i > work:
                priorities += [work]
                break
        else:
            answer += 1
            if current == location:
                break
    return answer

p = list(map(int, input()))
l = int(input())
print(solution(p, l))