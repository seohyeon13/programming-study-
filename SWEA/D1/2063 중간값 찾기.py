N = int(input())

num_list = list(map(int, input().split()))

num_list.sort() # 정렬

print(num_list[len(num_list)//2])