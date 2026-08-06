number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user():
    pass


many_user = [{'이름':'김시습',
              '나이':20,
              '주소':'서울'},
              {'이름':'허균',
              '나이':16,
              '주소':'강릉'},
              {'이름':'남혜인',
              '나이':25,
              '주소':'조선'},]

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book-=number

def rental_book(info):
    for name, age in info.items():
        rental_count = age//10
        decrease_book(rental_count)
        print(f'{name}님이 {rental_count}권의 책을 대여하였습니다.')

user_info = []

for user in many_user:
    info = {user['이름']:user['나이']}
    user_info.append(info)

for info in user_info:
    rental_book(info)

