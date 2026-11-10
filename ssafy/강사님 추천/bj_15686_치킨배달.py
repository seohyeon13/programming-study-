# N = 도시 크기, M = 치킨집 개수
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 좌표
chicken_pos = []
# 집 좌표
house_pos = []
# 치킨집 선택 조합
combination_chicken = []

# 최소값
min_distacne = float('inf')

# 1. 치킨집 위치 리스트에 넣기, 집 위치 넣기
for i in range(N):
    for j in range(N):
        if city[i][j] == 1: # 집
            house_pos.append((i,j))
        elif city[i][j] == 2: # 치킨
            chicken_pos.append((i,j))

# 1. 치킨집 M개의 조합
def combination(depth, idx):
    if depth == M:
        for house in house_pos: # 집 위치 순회
            for chicken in combination_chicken:
                distance = abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])
                mi

        return

    for i in range(idx, len(chicken_pos)):
        # 2. 해당 조합의 치킨집 좌표 리스트에 넣기
        combination_chicken.append(chicken_pos[i])
        combination(depth+1, idx+1)
        combination_chicken.pop()
        

# 3. 배열 순회 -> 1(집)에서 조합별 치킨집 최소 거리 구하기
# 4. 최소 거리 업데이트

combination(0,0)