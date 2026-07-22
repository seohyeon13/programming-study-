T = int(input())

for test_case in range(1, T+1):
    # 월 : 1 <= month <= 12
    # 첫번째 날짜 < 두번재 날짜

    month, day, month2, day2 = map(int, input().split())

    # 월별 마지막 리스트
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

    if month == month2:
        passed_day = day2-day
    else:
        passed_day = (day_list[month-1] - day) + day2

        for i in range(1,month2-month):
            passed_day += day_list[month+i-1]
    
    print(f'#{test_case} {passed_day+1}')