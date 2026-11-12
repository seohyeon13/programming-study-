T = int(input())

def check_films(films):
    # A(0) 먼저 검사
    for col in range(W): # 열 순회
        cell_cnt = 1
        for row in range(1,D): # 행
            if films[row][col] == films[row-1][col]:
                cell_cnt += 1
            else:
                cell_cnt = 1

            if cell_cnt >= K:
                break

        if cell_cnt < K: 
            return 0

    return 1
        
def dfs(row, cnt): 
    # row : 현재 행, cnt : 약품 처리 횟수
    global answer
    if cnt >= answer:
        return
    
    if row == D: # 행이 D라면 전체 행 돌아본 것.
        if check_films(films):
            answer= min(answer, cnt)
        return

    # 1. 약품 처리 전 원래 상태 검사
    dfs(row+1, cnt)

    # 2. A약품 처리
    before_A = films[row]
    films[row] = [0]*W
    dfs(row+1, cnt+1)
    films[row] = before_A # 원복

    # 3. B약품 처리 (1)
    before_B = films[row]
    films[row] = [1] * W
    dfs(row+1, cnt+1)
    films[row] = before_B # 원복

    
for tc in range(1, T+1):
    # D : 두께 (줄)
    # W : 가로 크기 (한 줄에 몇개)
    # K : 합격 기준 (세로 방향의 셀들이 K개 이상 연속적으로 있는 경우)
    D, W, K = map(int, input().split())

    films = [list(map(int, input().split())) for _ in range(D)]
    answer = float('INF') # 횟수 저장

    dfs(0, 0)

    print(f'#{tc} {answer}')