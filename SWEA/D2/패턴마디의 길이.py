T = int(input())

for test_case in range(1, T + 1):
    s = input()

    s2 = ""

    for i in range(1,10):
        if s[:i] == s[i:i+i]: #문자열 하나씩 늘려가며 비교
            s2 = s[:i]
            break

    print(f'#{test_case} {len(s2)}')


#     T = int(input())

# for test_case in range(1, T + 1):
#     s = input()

#     s2 = ""

#     for i in range(1,10):
#         if s[:i] == s[i:i+i]: #문자열 하나씩 늘려가며 비교
#             s2 += s[:i]

#     #print(s2)

#     print(f'#{test_case} {len(s2)}')