T = int(input())

for test_case in range(1, T + 1):
    month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31] # 월별 날짜 리스트

    date = input()

    year = date[:4] 
    month = int(date[4:6])
    day = int(date[6:])
    #print(year, month, day)
    if (month in month_list) and (day>0 and day<=day_list[month-1]):
        print(f'#{test_case} {date[:4]}/{date[4:6]}/{date[6:]}')
    else:
        print(f'#{test_case} -1')