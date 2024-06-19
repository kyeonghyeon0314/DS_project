# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.
    # 입력 힌트
    stack = []
    result = 0
    output = ""

    for char in input:
        if char == '(':
            stack.append(char)
            output += char
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += 1
                output = '(' + output
            output += char    
    
    while stack:
        stack.pop()
        result += 1
        output += ')'

    print(output)    

    return result

result = problem2(input)

print(result)
assert result == 3
print("정답입니다.")
