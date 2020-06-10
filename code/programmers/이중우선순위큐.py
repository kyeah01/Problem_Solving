queue = []

def binarySearch(num):
    s = 0
    e = len(queue)
    m = (s + e) // 2
    while s < e:
        m = (s + e) // 2
        if queue[m] == num:
            return m
        elif queue[m] < num:
            s = m + 1
        else:
            e = m - 1
    if s == 0:
        if len(queue) < 1 or queue[0] >= num:
            return s
        return s+1
    if len(queue) <= s:
        if queue[-1] <= num:
            return s
        return s-1
    if queue[s] > num:
        return s
    return s+1

def solution(operations):
    for direction in operations:
        print(queue)
        if direction == 'D 1':
            if queue:
                queue.pop(-1)
        elif direction == 'D -1':
            if queue:
                queue.pop(0)
        else:
            num = direction.split(' ')[1]
            position = binarySearch(int(num))
            queue.insert(position, int(num))
    if queue:
        return [queue[-1], queue[0]]
    return [0,0]
