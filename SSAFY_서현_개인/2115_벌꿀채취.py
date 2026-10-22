T = int(input())

for tc in range(1,T+1):
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 1. 행 순회 (0, N-M+1)
    # 2. i, i+1 선택
    # 3. 

    print(f'#{tc} ')