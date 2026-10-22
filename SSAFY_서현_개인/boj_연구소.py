import copy
from collections import deque

# N : 세로, M : 가로
N, M = map(int, input().split()) 

lab = [list(map(int, input().split())) for _ in range(N)] # 실제 연구소 맵


# 1. 벽을 세울 곳 리스트 저장 (0) -> empty리스트
# 2. 벽 세우는 조합 계산
# 3. 벽을 3개 세우면 안전 영역 계산 -> 리스트에 안전 영역 삽입
# 4. 리스트 중에 최대값 출력

comb_wall = [] # 벽 조합 리스트
empty = []
safe_area = []

dx = [-1, 1, 0, 0] # 상.하.좌.우
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i,j))

def virus(lab_map, wall): # 바이러스 확산
    for pos in wall: # 벽 세운 좌표
        lab_map[pos[0]][pos[1]] = 1 # 벽을 세웠으니 1로 표시

    # 바이러스 확산 -> bfs ...?
    q = deque()
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 2:
                q.append((i,j))

    while q:
        curr_x, curr_y = q.popleft()

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 2
                q.append((nx,ny))

# 1. 벽 세우는 조합 구하기 (DFS)
def combination(depth, idx):
    if depth == 3:
        # 영역 계산 해야 함.
        lab2 = copy.deepcopy(lab) # 벽 세우고 난 후 영역 계산 용
        virus(lab2, comb_wall)
        cnt = 0
        for i in range(N):
            cnt+=lab2[i].count(0)
        safe_area.append(cnt)
        return
    
    for i in range(idx, len(empty)):
        comb_wall.append(empty[i])
        combination(depth+1, i+1)
        comb_wall.pop()

combination(0,0)
print(max(safe_area))