# 함수 정의 : 정렬된 리스트에서 특정 숫자를 찾는 함수
def find_num(arr, a):
    if a in arr:
        return True
    else:
        return False

arr = [2, 4, 6, 8, 10]

print(arr)
print(f"{5} => {find_num(arr, 5)}")
print(f"{10} => {find_num(arr, 10)}")
