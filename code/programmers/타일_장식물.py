def solution(N):
    sequence = [1, 1]
    if N == 1: return 4
    if N == 2: return 6
    seqLen = len(sequence)
    while N > seqLen:
        sequence += [sequence[-2] + sequence[-1]]
        seqLen += 1
    return sequence[N-1] * 4 + sequence[N-2] * 2
