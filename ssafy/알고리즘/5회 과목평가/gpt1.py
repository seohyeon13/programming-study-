T =int(input())
num_list='0123456789ABCDEF'
for tc in range(1,T+1):
    num = input()
    answer = '' 

    int_num = num_list.index(num)
    
    for _ in range(4):
        answer = str(int_num%2)+answer
        int_num//=2
    print(f'#{tc} {answer}')

    

