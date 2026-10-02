T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 맵 크기

    hunter_map = [list(map(int, input().split())) for _ in range(N)]

    pos = [(0,0)]

    comb_list = []
    dis_list = []
    for i in range(N):
        for j in range(N):
            if hunter_map[i][j] < 0 or hunter_map[i][j] >0:
                pos.append((i,j))

    def comb(depth):
        if depth == len(pos):
            distance = abs(comb_list[0][0] - comb_list[1][0]) + abs(comb_list[0][1] - comb_list[1][1])
            dis_list.append(distance)
            return

        for i in range(len(pos)):
            if visited[i] == 0:
                visited[i] = 1
                comb_list.append(pos[i])
                comb(depth+1)
                comb_list.pop()
                visited[i] = 0

    visited = [0]*len(pos)
    comb(0)
