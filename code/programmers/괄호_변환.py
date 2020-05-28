def isItRight(string):
    blankCnt = 0
    for s in string:
        if s == '(':
            blankCnt += 1
        elif s == ')':
            if blankCnt == 0:
                return False
            blankCnt -= 1
    return True

def stringSplit(string):
    blankCnt = 1 if string[0] == '(' else -1
    for i in range(1, len(string)):
        if blankCnt == 0:
            return string[:i], string[i:]
        if string[i] == '(':
            blankCnt += 1
        else:
            blankCnt -= 1
    return string, ''

def solution(p):
    if isItRight(p) == True:
        return p
    u, v = stringSplit(p)
    if isItRight(u) == True:
        return u + solution(v)
    else:
        v = '(' + solution(v) + ')'
        for b in u[1:-1]:
            if b == '(':
                v += ')'
            else:
                v += '('
    return v
