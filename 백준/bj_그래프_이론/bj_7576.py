from collections import deque

# 상자 크기 (가로, 세로)
N,M = map(int, input().split())

# 0~(N-1), 0~(M-1)
mat = [[0]*(N) for i in range(M)]
 
q = deque()

for i in range(M):
    s = list(map(int, input().split()))
    for j in range(N):
        if s[j] == 1:
            q.append((i,j)) # 1 저장. (익은 토마토의 위치)
        
        mat[i][j] = s[j]

# 이동 위치
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    while q:
        x, y = q.popleft() #큐에 있는 위치 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<=(M-1) and 0<=ny<=(N-1)):
                if mat[nx][ny] == 0:
                    mat[nx][ny] = mat[x][y] + 1
                    q.append((nx, ny))


bfs() 

maxi = 0

for i in range(M):
    for j in range(N):
        if mat[i][j] == 0:
            print(-1)
            exit()
        
        if mat[i][j] > maxi:
            maxi = mat[i][j]

print(maxi-1)
    
'''
for i in range(M):
    for j in range(N):
        print(mat[i][j], end = ' ')
    print()
    '''