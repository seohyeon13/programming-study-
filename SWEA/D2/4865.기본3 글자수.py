T = int(input())

for i in range(T):
    s1 = input()
    s2 = input()

    cnt = 0
    max_cnt = 0

    for item in s1:
        if item in s2:
            cnt = s2.count(item)
        else:
            cnt = 0

        if cnt>=max_cnt:
            max_cnt = cnt
    
    print(f'#{i+1} {max_cnt}')