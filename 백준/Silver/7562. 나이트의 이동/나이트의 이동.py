from collections import deque

T = int(input())

dx = [-2, -2, 2, 2, -1, 1, -1, 1] # 상 하 좌 우
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

def bfs(x, y):
    global result
    q = deque()
    q.append((x, y))  # 현재 위치 큐에 삽입
    visited[x][y] = 1

    while q:
        cur_x, cur_y = q.popleft()

        if cur_x == target_x and cur_y == target_y:
            return visited[cur_x][cur_y] -1

        for d in range(8):
            nx = cur_x + dx[d]
            ny = cur_y + dy[d]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[cur_x][cur_y]+1
    
for tc in range(T):
    l = int(input()) # 체스판 한변의 길이
    x, y = map(int, input().split()) # 나이트가 현재 있는 칸
    target_x, target_y = map(int, input().split()) # 나이트가 이동하려고 하는 칸

    visited = [[0]*l for _ in range(l)]
    
    result = bfs(x, y)

    print(result)