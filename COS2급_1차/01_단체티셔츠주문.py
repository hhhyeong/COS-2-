# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(shirt_size):
    answer = [0,0,0,0,0,0]
    shirtsizelen = len(shirt_size)
    for i in range(0, shirtsizelen):
        # print(str(i) + " : " + shirt_size[i]);
        if shirt_size[i] == "XS":
            answer[0] += 1;
        elif shirt_size[i] == "S":
            answer[1] += 1;
        elif shirt_size[i] == "M":
            answer[2] += 1;
        elif shirt_size[i] == "L":
            answer[3] += 1;
        elif shirt_size[i] == "XL":
            answer[4] += 1;
        elif shirt_size[i] == "XXL":
            answer[5] += 1;
    return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print("solution 함수의 반환 값은", ret, "입니다.")


###################### 실행 결과값 ###################
# python3 01_단체티셔츠주문.py 
# solution 함수의 반환 값은 [1, 2, 0, 2, 1, 0] 입니다.