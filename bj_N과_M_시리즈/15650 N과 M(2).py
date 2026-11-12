N, M = map(int, input().split())

# 중복없이 M개 수열
# 고른 수열 오름차순

num_list = []

def dfs(start):
    if len(num_list) == M:
        print(*num_list)
        return

    for num in range(start, N+1):
        if num not in num_list:
            num_list.append(num)
            dfs(num+1)
            num_list.pop()

dfs(1)