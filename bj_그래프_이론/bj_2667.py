N = int(input())

mat = [[0]*(N) for i in range(N)]
visited = [[0]*(N) for i in range(N)]

for i in range(N):
    s = list(map(int, input()))
    for j in range(N):
        mat[i][j] = s[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

def dfs(x, y):
    stack = [(x,y)]

    while stack:

        global cnt 

        x, y = stack.pop()
        cnt+=1
        mat[x][y]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if mat[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))

for i in range(N):
    for j in range(N):
        if mat[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)
            


        