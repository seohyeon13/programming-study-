def sum_sequence(idx):
    global sum_number, cnt

    if sum_number == K:
        cnt+=1
        return

    for i in range(idx, N):
        sum_number += num_list[i]
        sum_sequence(i+1)
        sum_number -= num_list[i]
        
    


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split()) 

    num_list = list(map(int, input().split()))

    sum_number = 0
    cnt = 0
    sum_sequence(0)

    print(f'#{test_case} {cnt}')