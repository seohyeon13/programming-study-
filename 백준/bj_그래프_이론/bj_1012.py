T = int(input()) # 테스트 케이스 갯수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x,y):
    global cnt
    stack = [(x,y)]

    while stack:
        x, y = stack.pop()
        cnt+=1
        mat[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < M and 0<= ny < N:
                if mat[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))
    

    
for i in range(T):
    # M : 가로, N : 세로, K = 배추가 심어져있는 위치 갯수
    M,N,K = map(int, input().split())

    mat= [[0] * (N+1) for i in range(M+1)]
    visited = [[0] * (N+1) for i in range(M+1)]
    result = []


    for i in range(K):
        x, y = map(int, input().split())
        mat[x][y] = 1
            
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                cnt = 0
                dfs(i,j)
                result.append(cnt)
    
    print(len(result))
        
