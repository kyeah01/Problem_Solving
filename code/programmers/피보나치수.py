result = [0,1,1,2,3,5]

def solution(n):
    global result
    if len(result) > n:
        return result[n]
    now = len(result)-1
    while now != n:
        result += [(result[now-1] + result[now]) % 1234567]
        now += 1
    return result[n]
