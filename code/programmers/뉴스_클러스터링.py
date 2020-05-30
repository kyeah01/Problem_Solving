def strSetMaker(string):
    return [
        string[i:i+2].lower()
        for i in range(len(string)-1)
        if string[i:i+2].isalpha()
    ]

def solution(str1, str2):
    str1 = strSetMaker(str1)
    str2 = strSetMaker(str2)

    if len(str1) == 0 and len(str2) == 0:
        jaccard = 1
    else:
        unionLen, intersectionLen = 0, 0
        for s in (set(str1) | set(str2)):
            unionLen += max(str1.count(s), str2.count(s))
            intersectionLen += min(str1.count(s), str2.count(s))
        jaccard = intersectionLen / unionLen
    return int(jaccard * 65536)
