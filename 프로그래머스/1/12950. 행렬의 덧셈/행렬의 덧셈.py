def solution(arr1, arr2):
    answer =[]
    for i in range(len(arr1)):
        row = []
        for k in range(len(arr1[i])):
            row.append(arr1[i][k] + arr2[i][k])
        answer.append(row)
    return answer