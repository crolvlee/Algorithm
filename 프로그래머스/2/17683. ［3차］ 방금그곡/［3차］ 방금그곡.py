# 네오가 기억하고 있는 멜로디: 음악의 끝과 처음이 이어진 것일 수도

# 음은 1분에 1개씩 재생됨
# 음악은 무조건 처음부터 재생됨

# C# -> X
# D# -> Y
# F# -> Z
# G# -> M
# A# -> N

def convert_sharp(now):
    now = now.replace('C#', 'X')
    now = now.replace('D#', 'Y')
    now = now.replace('F#', 'Z')
    now = now.replace('G#', 'M')
    now = now.replace('A#', 'N')
    now = now.replace('B#', 'O') # 테스트
    
    return now
                  

def solution(m, musicinfos):
    listen_m = convert_sharp(m)
    result_list = []
    
    for idx in range(len(musicinfos)):
        musicinfo = musicinfos[idx]
        start_time, end_time, name, book = musicinfo.split(",")
        
        # 1. 시간 구하기
        start_time_point = int(start_time[0:2]) * 60 + int(start_time[3:5])
        end_time_point = int(end_time[0:2]) * 60 + int(end_time[3:5])
        time = end_time_point - start_time_point

        # 2. 샵 붙은 것 바꿔주기
        book_str = convert_sharp(book)
        
        # 3. 주어진 시간 동안 재생되는 음
        play_book = ""
        for i in range(time):
            play_book += book_str[i % len(book_str)]
            
        # 4. 주어진 시간 동안 재생되는 음에 listen_m이 있는지 확인
        if listen_m in play_book:
            # 이름, 재생된 시간, 음악 인덱스
            result_list.append([-time, idx, name])
    
        
    answer = ''
    
    if len(result_list) > 0:
        result_list.sort()
        answer = result_list[0][2]
    else:
        answer = '(None)'
    
    return answer