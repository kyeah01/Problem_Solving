def solution(triangle):
    curr = triangle[-1]
    for tri in triangle[-2::-1]:
        curr = [max(curr[i], curr[i+1]) + tri[i] for i in range(len(tri))]
    return curr[0]
