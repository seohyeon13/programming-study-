T = int(input())

for test_case in range(1, T + 1):

    num_list = list(map(int, input().split()))

    avg = sum(num_list)/len(num_list)

    print(f'#{test_case} {avg:.0f}')