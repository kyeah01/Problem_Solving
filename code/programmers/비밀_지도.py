def mapMaker(n, arr):
    return [
        '0' *(n-len(bin(arr[i])[2:])) + bin(arr[i])[2:]
        for i in range(len(arr))
    ]

def solution(n, arr1, arr2):
    arr1 = mapMaker(n, arr1)
    arr2 = mapMaker(n, arr2)
    return [
        ''.join([
            '#' if arr1[i][j] == '1' or arr2[i][j] == '1' else ' '
            for j in range(n)
        ])
        for i in range(n)
    ]
