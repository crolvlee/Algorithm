def solution(record):
    nickname_db = {}
    actions_db = []
    
    db = []
    for r in record:
        if r[0] == "E":
            action, uid, nickname = r.split()
            # 닉네임 db에 넣기
            nickname_db[uid] = nickname     # 딕셔너리에 이미 있으면 대체됨
            # actions에 넣기
            actions_db.append([uid, 'Enter'])
            
        elif r[0] == "C":
            action, uid, nickname = r.split()
            # 닉네임 db에 이름 수정
            nickname_db[uid] = nickname     # 딕셔너리에 이미 있으면 대체됨
            
        elif r[0] == "L":
            action, uid = r.split()
            # actions에 넣기
            actions_db.append([uid, 'Leave'])
            
    
    answer = []
    
    for a in actions_db:
        uid = a[0]
        nickname = nickname_db[uid]
        action = a[1]
        
        if action == 'Enter':
            sentence = nickname + '님이 들어왔습니다.'
        elif action == 'Leave':
            sentence = nickname + '님이 나갔습니다.'
        
        answer.append(sentence)

    
    return answer


