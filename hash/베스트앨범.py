def solution(genres, plays):
    answer = []
    
    # 여기서 이제 장르별로 play 횟수를 만들고 내림차순정렬
    genre_dict = {}
    for i, genre in enumerate(genres):
        if genre not in genre_dict:
            genre_dict[genre] = plays[i] 
        else:
            genre_dict[genre] += plays[i]
    sorted_genre_play = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
    
    # 여기서는 장르별로 play 높은 인덱스 순서로 내림차순정렬
    genre_indices = {}
    for index, genre in enumerate(genres):
        if genre not in genre_indices:
            genre_indices[genre] = [index]
        else:
            genre_indices[genre].append(index)
    # 위에는 우선 장르별 인덱스 다 넣기 
    # 바로 밑에는 장르별 인덱스 정렬하기
    for genre in genre_indices:
        genre_indices[genre].sort(key=lambda i: plays[i], reverse=True)
    
    # 이제 여기서 횟수가 높은 장르 순서대로 인덱스 높은거 최대 2개 뽑아내기
    for genre, _ in sorted_genre_play:
        top_indices = genre_indices[genre][:2] 
        answer.extend(top_indices) 
        
    return answer