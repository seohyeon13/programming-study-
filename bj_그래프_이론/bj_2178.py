from collections import deque

# N X M 미로
N, M = map(int, input().split())

mat = [[0] * M for i in range(N)]

for i in range(N):
    s = list(map(int,input()))
    for j in range(M):
        mat[i][j] = s[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0)) # 시작점 

    while queue:
        x, y = queue.popleft()

        for i in range(4): #행
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx <N and 0<= ny <M:
                if mat[nx][ny] == 1:
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append((nx, ny))
        
    return mat[N-1][M-1]

print(bfs())

        

    





