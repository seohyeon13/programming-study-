'''
버스 노선 : N개
i번째 버스 노선은 번호가 Ai 이상
Bi이하인 모든 정류장만을 다니는 버스 노선
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하기


'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    busstops = [0]*5001 # 5000개의 버스 정류장
    for i in range(N):
        A,B = map(int, input().split())
        for j in range(A, B+1):
            busstops[j] += 1  
    P = int(input())
    buses = []
    for i in range(P):
       idx = int(input())
       buses.append(busstops[idx])

    print(f'#{tc} ', *buses)


