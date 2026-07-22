T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    num_list = list(map(int, input().split()))

    print(f'#{test_case}', end = ' ')
    
    sorted_list = sorted(num_list)

    for num in sorted_list:
        print(num, end = ' ')
    print()