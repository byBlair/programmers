def solution(phone_number):
    length = len(phone_number)
    #뒷 4자리를 제외한 부분을 '*'로 대체하고, 뒷 4자리와 합칩니다.
    return '*' * (length - 4) + phone_number[-4:]
    return answer