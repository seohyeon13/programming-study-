# dfs , bfs 
from collections import deque

N, M, V = map(int, input().split()) # N : 정점 갯수, M : 간선 갯수, V : 시작 정점 번호

matrix = [[0] * (N+1) for i in range(N+1)]

for i in range(M): # 간선 갯수만큼 반복
    u1, u2 = map(int, input().split())
    matrix[u1][u2] = 1
    matrix[u2][u1] = 1

def dfs(matrix, start, visited):
    stack = [start]
    while stack:
        value = stack.pop()
        if visited[value] == 0:
            print(value, end = ' ')
            visited[value] = 1

        for i in range(N,0,-1):
            if matrix[value][i] == 1 and (visited[i] == 0):
                stack.append(i)


def bfs(matrix, start, visited):
    q = deque()
    q.append(start)

    while q:
        value = q.popleft()
        if visited[value] == 0:
            print(value, end = ' ')
            visited[value]=1

        for i in range(N+1):
            if matrix[value][i] == 1 and (visited[i]==0):
                q.append(i)

visited = [0] * (N+1)
dfs(matrix, V, visited)

print()

visited = [0] * (N+1)
bfs(matrix, V, visited)

'''
for i in range(N):
    for j in range(N):
        print(matrix[i][j],end = ' ')
    print(" ")
'''

