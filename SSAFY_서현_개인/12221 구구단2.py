T = int(input())

for test_case in range(1,T+1):
    A, B = map(int, input().split())

    if A > 9 or B > 9:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {A*B}')