from collections import deque
# M:가로(열) , N : 세로 (행)
M, N = map(int, input().split())

tomato_box = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

day = 0

q = deque()

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            q.append((i,j))

def bfs():
    global day
    while q:

        for _ in range(len(q)):
            curr_x, curr_y = q.popleft()

            for i in range(4):
                nx = curr_x + dx[i]
                ny = curr_y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue

                if tomato_box[nx][ny] == 0:
                    tomato_box[nx][ny] = 1
                    q.append((nx,ny))
        day+=1
                
bfs()

cnt = 0
for i in range(N):
    cnt += tomato_box[i].count(0)

if cnt > 0:
    print(-1)
else:
    print(day-1)


