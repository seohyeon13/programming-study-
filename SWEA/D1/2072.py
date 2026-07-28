T = int(input())

for test_case in range(1, T + 1):

    num_list = list(map(int, input().split()))
    sum = 0
    for num in num_list:
        if num % 2 != 0:
            sum += num


    print(f'#{test_case} {sum}')