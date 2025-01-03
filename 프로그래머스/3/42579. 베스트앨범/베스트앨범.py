# 모든 장르는 재생된 횟수 다름!

def solution(genres, plays):
    
    # 장르별 노래들 정보 (노래 재생 수, 노래 번호)
    genre_dict = {}
    
    for i, genre in enumerate(genres):
        if genre not in genre_dict:
            genre_dict[genre] = [[plays[i], i]]
        else:
            genre_dict[genre].append([plays[i], i])
    
    # 장르별 노래들 정보 정렬
    for genre_name, genre_list in genre_dict.items():
        sorted_genre_list = sorted(genre_list, key = lambda x:(-x[0], x[1]))
        genre_dict[genre_name] = sorted_genre_list
        
    # 장르별 총 재생수 카운트
    genre_cnt = []
    
    for genre_name, genre_list in genre_dict.items():
        time = 0
        for song in genre_list:
            time += song[0]
            
        genre_cnt.append([genre_name, time])
        
    genre_cnt.sort(key=lambda x:-x[1])
    
    # 장르별로 top2 골라서 answer에 넣기
    answer = []
    
    for genre_info in genre_cnt:
        genre_name = genre_info[0]
        
        # top1 넣기
        answer.append(genre_dict[genre_name][0][1])
        if len(genre_dict[genre_name]) >= 2:
            answer.append(genre_dict[genre_name][1][1])
        
        
    return answer