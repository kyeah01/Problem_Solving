def check(a, b):
    a = list(a)
    b = list(b)
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return True if cnt == 1 else False        

def solution(begin, target, words):
    queue = [(begin, [begin])]
    while queue:
        n = queue.pop(0)
        if n[0] == target:
            return len(n[1])-1
        # 찾아야 해 나랑 비슷한 애를, 그래서 걔를 넣어야돼 queue안에.
        for word in words:
            if check(n[0], word) and word not in n[1]:
                # 체크해봤더니 비슷하고, 이전에 썼던 것도 아님.
                queue += [(word, n[1]+[word])]
    return 0