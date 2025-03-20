def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):  # 두 번째 원소부터 비교 시작
        if arr[i] != arr[i - 1]:  # 이전 원소와 다르면 추가
            answer.append(arr[i])
    return answer
        