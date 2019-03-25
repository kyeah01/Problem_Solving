subin, bro = map(int, input().split())
time = 1

while True:
    # 수빈이가 이동한다. 동생과 같은 위치에 갈 수 있는지 알아낸다.
    # 수빈이와 동생이 같은 위치에 같은 시간에 있는지 확인한다.
    # 아니라면 동생은 다음 위치로 이동한다.
    # 동생을 이동시켜보자.
    bro += time
       if subin-time <= bro <= subin*2**time:
           
    time += 1