'''
각 숫자 -> 지형의 높이

1. 가장 높은 봉우리에서 시작
2. 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 -> 가로 / 세로 방향
3. 긴 등산로를 만들기 위해 딱 한 곳 정해서 최대 k깊이만큼 지형을 깎는 공사 할 수 있음


1. 최대값 찾기 (시작점)
2. 

'''
T = int(input())

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def dfs(x, y, path):
    global hiking_path
    # x, y 는 현재 좌표
    visited[x][y] = 1

    if hiking_path < path:
        hiking_path = max(path, hiking_path)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 1. 범위 밖 이동 x
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        # 방문햇으면 이동 x
        if visited[nx][ny]:
            continue

        # 2. 값이 크면 이동 x
        if arr[nx][ny] > arr[x][y]:
            continue
        if arr[nx][ny] == arr[x][y]:
            if K:
                pass

        dfs(nx, ny, path+1)

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    max_val = 0
    hiking_path = 0

    # 1. 최대값 찾기
    for i in range(N):
        for j in range(N):
            max_val = max(max_val, arr[i][j])

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                dfs(i, j, 0)


    




