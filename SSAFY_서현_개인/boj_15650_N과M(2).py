N, M = map(int, input().split())

visited = [0]*(N+1)
num_list = [] # 수열 담을 배열

def dfs(start_num):
    if len(num_list) == M:
        print(*num_list)
        return

    for num in range(start_num, N+1):
        if visited[num] == 0:
            visited[num] = 1
            num_list.append(num)
            dfs(num+1)
            num_list.pop()
            visited[num] = 0

dfs(1)