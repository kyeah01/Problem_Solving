def solution(n):
    answers = [0, [0], [0,0,1], [0,0,1,0,0,1,1]]
    i = len(answers) - 1
    while i < n:
        answers += [answers[i] + [0] + [abs(a-1) for a in answers[i][::-1]]]
        i += 1
    return answers[n]
