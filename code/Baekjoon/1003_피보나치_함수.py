fibo = [[1,0], [0,1]]

for _ in range(int(input())):
    n = int(input())
    if len(fibo) > n:
        print(*fibo[n])
    else:
        for i in range(len(fibo), n+1):
            fibo += [[fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]]]
        print(*fibo[-1])