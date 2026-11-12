N, M = map(int, input().split())

num_list = []

def dfs(start):
    if len(num_list) == M:
        print(*num_list)
        return

    for num in range(start,N+1):
        # if num not in num_list:
            num_list.append(num)
            dfs(num)
            num_list.pop()

dfs(1)