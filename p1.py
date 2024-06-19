# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    # 이곳에 코드를 작성하세요.
    mean = 0 
    median = 0 
    result = [0,0] 
    
    
    mean = sum(input)/len(input) 

    input.sort() 
    x = len(input) 
    if x%2 == 0: 
        x = (x-1)/2
        median = input[x]
    else: 
        x = x // 2
        median = input[x]



    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
