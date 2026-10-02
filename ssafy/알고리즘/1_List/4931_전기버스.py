'''
한번 충전으로 이동할 수 있는 정류장 수 정해져 있음
버스 : 0번부터 출발 ~ 종점 N번 정류장까지 이동
한번 충전으로 최대한 이동할 수 있는 정류장 수 K
M : 충전기가 설치된 정류장 번호의 개수
최소한 몇번의 충전을 해야 종점에 도착할 수 있을까?

종점 도착 불가 = 0
출발지에는 충전기 설치 O -> 횟수에는 포함되지 X


K : 3 (한번 충전으로 최대한 이동할 수 있는 정류장 수)
N : 10 (정류장 번호)
M : 5 (충전기가 설치된 정류장 수)
'''

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    buses = list(map(int,input().split()))
    answer = 0 # 도착 불가면 0이니까. 기본값은 0
    cur = 0 # 현재 정류장
    while True:
        # 도착점 이상
        next_bus = cur + K
        if next_bus >= N:
            break

        # 도착점이 아니라면
        temp = next_bus
        found = False
        while temp>cur:
            if temp in buses: 
                cur = temp
                answer += 1
                found = True
                break
            temp -= 1

        # 충전소 찾았으면
        if not found:
            answer = 0
            break    
    print(f'#{tc} {answer}')