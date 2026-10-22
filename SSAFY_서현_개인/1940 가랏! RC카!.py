T = int(input())

for test_case in range(1, T+1):
    # 커맨드 수
    N = int(input())

    # 이동거리
    distance=  0

    # 현재 속도
    curr_velocity = 0

    # 각 테스트케이스만큼 반복
    for _ in range(N):
        
        # 명령과 속도
        command = list(map(int, input().split()))

        if command[0] == 1: # 1이면 가속
            curr_velocity += command[1]
            distance += curr_velocity
        elif command[0] == 2: # 2면 감속
            if command[1] > curr_velocity:
                distance = 0
            else:
                curr_velocity -= command[1]
                distance += curr_velocity
        else: # 0이면
            distance += curr_velocity

    print(f'#{test_case} {distance}')