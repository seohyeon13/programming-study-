def queen(x):
    for y in range(N):
        queen_position[x] = y

        





T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    queen_position = [0]*N

    queen(0) # 0번째 행에 퀸 놓고 있음


