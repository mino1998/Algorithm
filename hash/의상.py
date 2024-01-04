from collections import Counter

def solution(clothes):
    clothes_dict=Counter([clothe[1] for clothe in clothes])
    count =1
    for count_clothes in clothes_dict.values():
        count=count*(count_clothes+1)
    return count-1