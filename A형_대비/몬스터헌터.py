T = int(input())

def dfs(level, r, c, time):
    global answer

    if time >= answer:
        return # 크다면 고려할 필요 없음. 최소 시간을 찾아야 하기 때문

    if level == len(targets): 
        answer = min(answer, time) # 최소 시간 갱신
        return

    for i in range(len(targets)):
        if visited[i]: # 방문했다면 x
            continue

        nr, nc, val = targets[i]  # 방문

        if val < 0 and not hunted[abs(val)]: # 헌터인데, 해당 값의 몬스터 사냥 안햇을 경우
            continue

        distance = abs(r-nr) + abs(c-nc)

        visited[i] = 1

        if val > 0: # 몬스터라면
            hunted[val] = 1

        dfs(level+1, nr, nc, time + distance)

        if val > 0:  # 원복
            hunted[val] = 0

        visited[i] = 0 # 원복


for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    targets = [] # 몬스터 or 헌터 좌표 및 값 저장
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                targets.append((r,c,arr[r][c])) # 행, 열, 좌표값

    answer = float('inf') # 최소 시간

    visited = [0]*(len(targets))

    hunted = [0]*(len(targets)//2 + 1) # 몬스터 사냥 여부 확인

    dfs(0, 0, 0, 0)

    print(f'#{tc} {answer}')