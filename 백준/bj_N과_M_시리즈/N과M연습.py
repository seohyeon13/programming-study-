def combination(depth, num):
    if depth == M:
        print(*num_list)
        return

    for i in range(num,N+1):
            num_list.append(i)
            combination(depth+1, i+1)
            num_list.pop()
        

N, M = map(int, input().split())

num_list = []
combination(0, 1)