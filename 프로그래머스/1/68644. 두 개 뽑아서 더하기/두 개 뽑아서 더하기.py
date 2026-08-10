def solution(numbers):
    answer = set()
    s = sorted(numbers)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            answer.add(s[i] + s[j])
    return sorted(answer)