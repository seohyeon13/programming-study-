def check_films():
    if K == 1:
        return 1
    all_pass = 0

    for c in range(W):
        cell = films[0][c]
        count_cell = 1

        for r in range(1, D):

            if films[r][c] == cell:
                count_cell += 1
                if count_cell == K:
                    all_pass += 1
                    break
            else:
                count_cell = 1
                cell = films[r][c]

    if all_pass == W:
        return 1
    else:
        return 0


def dfs(row, cnt):
    global answer

    if answer <= cnt:
        return
    
    if row == D:
        if check_films():
            answer = min(answer, cnt)
        return

    # 아무것도 처리 x
    dfs(row+1, cnt)

    # A로 변경
    backup_A = films[row]
    films[row] = [0]*W
    dfs(row+1, cnt+1)
    films[row] = backup_A

    # B로 변경
    backup_B = films[row]
    films[row] = [1]*W
    dfs(row+1, cnt+1)
    films[row] = backup_B


T = int(input())

for tc in range(1, T+1):
    # D : 필름 두께, W : 가로크기, K : 합격기준
    D, W, K = map(int,input().split())

    films = [list(map(int, input().split())) for _ in range(D)]

    answer = K

    dfs(0, 0)
    print(f'#{tc} {answer}')