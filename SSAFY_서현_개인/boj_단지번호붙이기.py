from collections import deque

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)] # 방문표시

# 1. 이동방향
dx = [-1, 1, 0, 0] # 상.하.좌.우
dy = [0, 0, -1, 1]

# 한 단지 갯수 저장하기 위한 리스트
cnt_house = []

def bfs(x, y):
    global cnt
    q = deque()

    q.append((x,y))

    while q:
        curr_x, curr_y = q.popleft()
        cnt+= 1

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            # 범위 벗어나면
            if nx < 0 or nx >= N or ny < 0 or ny >=N:
                continue

            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

        
# 각 좌표들 순회
# 좌표 값이 1이거나(집 O) 방문하지 않은 곳은 탐색 시작
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 0
            bfs(i, j)
            cnt_house.append(cnt)

cnt_house.sort()
print(len(cnt_house))
for i in range(len(cnt_house)):
    print(cnt_house[i])