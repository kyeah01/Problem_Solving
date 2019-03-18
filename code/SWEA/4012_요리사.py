def combination(arr, r):
    def generate(chosen):
        global answer
        if len(chosen) == r:
            answer += [chosen[:]]
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen += [arr[nxt]]
            generate(chosen)
            chosen.pop()
    generate([])
    return answer

T = int(input())
for tc in range(1, T+1):
    answer = []
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    A_cases = combination(list(range(N)), N//2)
    B_cases = [[i for i in range(N) if i not in A] for A in A_cases]
    minN = 40000
    for k in range(len(A_cases)):
        A_ingredient, B_ingredient = 0,0
        A_case, B_case = A_cases[k], B_cases[k]
        for i in range(N//2):
            for j in range(i+1, N//2):
                A_ingredient += synergy[A_case[i]][A_case[j]]+synergy[A_case[j]][A_case[i]]
                B_ingredient += synergy[B_case[i]][B_case[j]]+synergy[B_case[j]][B_case[i]]
        minN = min(minN, abs(A_ingredient-B_ingredient))
    print(minN)