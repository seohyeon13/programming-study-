T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))

    max_num = float('-INF')

    for num in num_list:
        if num > max_num:
            max_num = num
        
    print(f'#{test_case} {max_num}')