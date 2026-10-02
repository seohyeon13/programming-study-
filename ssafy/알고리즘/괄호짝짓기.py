for tc in range(1, 11):
    N = int(input())

    words = input()

    stack = []

    answer = 1

    for word in words:
        if word in '({[<':
            stack.append(word)
        else:
            if not stack: 
                answer = 0
                break

            top = stack.pop()

            if not((word == ')' and top == '(') or (word == ']' and top == '[') or (word == '}' and top == '{') or (word == '>' and top == '<')):
                answer = 0
                break

    if stack:
        answer = 0
    print(f'#{tc} {answer}')
                
            




            
        
