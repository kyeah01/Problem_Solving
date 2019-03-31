def car(k, pair_time, accum):
    global n, minN, total_distance
    # 최대거리를 넘어갈 경우 불가능함으로 쳐내는 조건.
    if accum > max_distance:
        return
    # 끝까지 갔을때
    if k == n:
        # 최대거리조건을 위반하지않는지 확인
        if accum + distance[k] <= max_distance:
            minN = min(minN, pair_time)
        return
    # 가지치기를 위한 조건, 글로벌 값보다 높아지면 바로 리턴되어버리게.
    if pair_time > minN:
        return 
    if accum + distance[k] <= max_distance:
        car(k+1, pair_time+times[k], 0)
        car(k+1, pair_time, accum+distance[k])

# main
max_distance = int(input())
n = int(input())
distance = list(map(int, input().split()))
times = list(map(int, input().split()))
minN = 10000000000
total_distance = sum(distance)
car(0, 0, 0)
print(minN)