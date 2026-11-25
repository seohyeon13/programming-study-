from collections import deque

# dfs, bfs 함수 각각 따로 

# N : 정점 갯수, M : 간선 갯수, V : 시작 정점 번호
N, M, V = map(int, input().split())

mat = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    mat[x][y] = 1
    mat[y][x] = 1

def bfs(matrix, visited, start):
    q = deque()
    q.append(start)

    while q:
        num = q.popleft()
        if visited[num] == 0:
            visited[num] = 1
            print(num, end = ' ')
        
        for i in range(N+1):
            if matrix[num][i] == 1 and visited[i] == 0:
                q.append(i)

def dfs(matrix, visited, start):
    stack = [start]
    
    while stack:
        num = stack.pop()
        
        if visited[num] == 0:
            visited[num] = 1
            print(num, end = ' ')
        
        for i in range(N, 0, -1):
            if matrix[num][i] == 1 and visited[i] == 0:
                stack.append(i)

visited = [0] * (N+1)
dfs(mat, visited, V)

print()

visited = [0] * (N+1)
bfs(mat, visited, V)
        



    