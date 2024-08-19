def solution(s):
    #문제 이해
    # - 입력: 일부 숫자가 영단어로 바뀐 "문자열"
    # - 출력: 원래 숫자
    # - 영단어 표를 코드로 구현
    #   - 영단어 표를 : 리스트
    #   - 영단어 표를 : 딕셔너리
    # - 입력받은 문자를 해당하는 숫자로 변환
    answer = 0
    word_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for idx, wl in enumerate(word_list):
        s = s.replace(wl, str(idx))
        
    return int(s) 