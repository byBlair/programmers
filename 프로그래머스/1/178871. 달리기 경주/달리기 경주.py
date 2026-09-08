def solution(players, callings):
    answer = []
    position = {}
    for i in range(len(players)):
        position[players[i]] = i
        
    for calling in callings:
        current = position[calling]
        front = current - 1
        player_front = players[front]
        
        #두 선수 자리 바꾸기
        players[front], players[current] = players[current] , players[front]
        
        #position 바뀐 위치로 업데이트
        position[calling] = front
        position[player_front] = current
        
    return players