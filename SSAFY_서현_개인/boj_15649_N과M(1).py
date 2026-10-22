# N, M = map(int, input().split())

# num_list = []

# # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# def dfs():

#     if len(num_list) == M:
#         print(*num_list)
#         return

            
#     for num in range(1, N+1): # 3
#         if num not in num_list:
#             num_list.append(num)
#             dfs()
#             num_list.pop()

# dfs()

N, M = map(int, input().split())

visited = [0]*(N+1)
num_list = [] # 수열 담을 배열

def dfs():
    if len(num_list) == M:
        print(*num_list)
        return

    for num in range(1, N+1):
        if visited[num] == 0:
            visited[num] = 1
            num_list.append(num)
            dfs()
            num_list.pop()
            visited[num] = 0

dfs()