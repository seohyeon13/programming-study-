T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
 
    # P : 금액, Q : 기본 요금, R : 기준 리터 , S : 초과량 금액, W : 한달간 사용하는 수도의 양
    P, Q, R, S, W = map(int, input().split())
 
    # A 사 : 리터당 P
    A_pay = W * P
 
    # B사 
    B_pay = Q
 
    if(W > R):
        over_used = W-R
        B_pay = Q + S*over_used #초과 금액
 
    print(f'#{test_case} {min(A_pay, B_pay)}')