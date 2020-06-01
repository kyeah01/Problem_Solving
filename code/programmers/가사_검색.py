# 정규표현식으로 풀이.
# 이 경우 효율성 테스트에서 40% 통과.

import re

def solution(words, queries):
    count = [0 for _ in queries]
    for i in range(len(queries)):
        q = '^' + ''.join(['.' if q=='?' else q for q in queries[i]]) + '$'
        p = re.compile(q)
        for word in words:
            if p.match(word) != None:
                count[i] += 1
    return count

