def solution(numbers):
    #문제이해
    # - 입력: 리스트
    # - 출력 : 리스트 평균(int)로 출력
    #아이디어
    # - 리스트의 총합을 구한다
    # - 리스트의 길이로 나눈다
    #제안사항
    # - numbers 의 원소가 : 1000
    # - numbers 길이: 100
    answer = 0
    for num in numbers:
        answer+=num
    return answer/len(numbers)