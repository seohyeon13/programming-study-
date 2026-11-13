'''
N : 세로
M : 가로
'''
from collections import deque

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def bfs(r, c, island):
    q = deque()
    q.append((r,c))
    arr[r][c] = island

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx<0 or nx>=N or ny < 0 or ny>=M:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = island
                q.append((nx,ny))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a == parent_b:
        return 0

    parent[b] = parent[a]
    return 1


# ===============================
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

island = 2

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            bfs(r, c, island)
            island+=1

cnt_island = island-2

edges = []

for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            continue

        start = arr[r][c] # 섬 번호

        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]
            length = 0

            while 0<= nr < N and 0<= nc <M:
                if arr[nr][nc] == start: # 섬 번호 일치(같은 섬이라면)
                    break 
                if arr[nr][nc] != 0: # 다른 섬 만난 것
                    if length >= 2: # 2이상이면
                        edges.append((length, start, arr[nr][nc])) # 간선에 저장
                    break

                length += 1
                nr += dx[d]
                nc += dy[d]

parent = [i for i in range(island)] # 0부터 island까지

edges.sort()

total = 0
cnt = 0

for cost, a, b in edges:
    if union(a,b):
        total += cost
        cnt+=1

if cnt == cnt_island - 1:
    print(total)
else:
    print(-1)

