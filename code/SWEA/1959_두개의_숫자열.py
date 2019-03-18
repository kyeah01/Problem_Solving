T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxN = 0
    if len(A) > len(B):
        A,B = B,A
    for i in range(len(B)-len(A)+1):
        answer = 0
        for j in range(len(A)):
            answer += A[j]*B[i+j]
            print(A[j]*B[i+j])
        maxN = max(answer, maxN)
    print(maxN)