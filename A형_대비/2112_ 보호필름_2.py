T = int(input())

def check_films(films):
    global answer
    all_pass = 0

    # A(0) 먼저 검사
    for col in range(W): # 열 순회
        first_num = films[0][col]
        cell_cnt = 0
        for row in range(1,D): # 행
            if films[row][col] == first_num:
                cell_cnt += 1
            else:
                if cell_cnt >= K:
                    cell_cnt += 1
                cell_cnt = films[row][col]
        if cell_cnt >= K:
            all_pass += 1

    if all_pass == W:
        answer += 1

def dfs(row): 
    if row == D: # 행이 D라면 전체 행 돌아본 것.
        # 1. 약품 처리 전 원래 상태 검사
        check_films(films)
        return

    dfs(row+1)

    # 2. A약품 처리
    before_A = films[row]
    films[row] = [0]*W
    dfs(row+1)
    films[row] = before_A # 원복

    # 3. B약품 처리 (1)
    before_B = films[row]
    films[row] = [1] * W
    dfs(row+1)
    films[row] = before_B # 원복


    
    
for tc in range(1, T+1):
    # D : 두께 (줄)
    # W : 가로 크기 (한 줄에 몇개)
    # K : 합격 기준 (세로 방향의 셀들이 K개 이상 연속적으로 있는 경우)
    D, W, K = map(int, input().split())

    films = [list(map(int, input().split())) for _ in range(D)]
    answer = 0 # 횟수 저장

    dfs(0)

    print(f'#{tc} {answer}')