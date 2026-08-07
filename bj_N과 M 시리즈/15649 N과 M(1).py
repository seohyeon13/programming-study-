N, M = map(int, input().split())

num_list = []

def dfs():
    if len(num_list)==M:
        print(*num_list)
        return

    for num in range(1, N+1):
        if num not in num_list:
            num_list.append(num)
            dfs()
            num_list.pop()

dfs()