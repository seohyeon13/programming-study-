for test_case in range(1,11):
    N = int(input())
    building_list = list(map(int, input().split()))

    cnt = 0

    for i in range(2,N-2):
        curr_building = building_list[i]
        max_building = building_list[i-2]
        for j in range(i-1, i+3):
            if j != i and building_list[j] > max_building:
                max_building = building_list[j]

        if curr_building > max_building:
            cnt += (curr_building - max_building)

    print(f'#{test_case} {cnt}')