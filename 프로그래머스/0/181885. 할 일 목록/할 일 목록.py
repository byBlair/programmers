def solution(todo_list, finished):
    answer = []
    for todo,fin in zip(todo_list, finished):
        if not fin: #done이 false
            answer.append(todo)
    return answer