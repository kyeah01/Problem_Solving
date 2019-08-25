for tc in range(1, int(input())+1):
    num = input()
    cnt = 0
    while len(num) > 1:
        if len(num) > 2:
	        num = str(int(num[0])+int(num[1])) + num[2:]
        else:
            num = str(int(num[0])+int(num[1]))
        cnt += 1
    print('A' if cnt%2 else 'B')