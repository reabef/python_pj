# 홀수 짝수 판별하기
no = 13

def noType(no):
    divide = no % 2
    if divide > 0 : 
        print("홀수 입니다")
    else :
        print("짝수 입니다")

noType(no)
