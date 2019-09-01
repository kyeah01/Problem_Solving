def powerset(k, arr, target):
    global n,cnt
    if sum(arr) == target:
        # au가 1인게 있으면 괜찮은거임
        for au in alreadyUsed:
            flag = False
            for x in range(n):
                if au[x] and not arr[x]:
                    flag = True
            if not flag:
                return
        if len(relation) == len({tuple(x[i] for i in range(len(arr)) if arr[i]) for x in relation}):
            alreadyUsed.append([i for i in arr])
            cnt += 1
        return
    if k == n:
        return
    arr[k] = 0
    powerset(k+1, arr, target)
    arr[k] = 1
    powerset(k+1, arr, target)

relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]

cnt = 0
n = len(relation[0])
alreadyUsed = []
for i in range(1, n+1):
    arr = [0]*n
    powerset(0, arr, i)
print(cnt)