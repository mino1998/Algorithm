#오답 1
#def solution(citations):
#    answer=[]
#    sort_citations=sorted(citations)
#    unique_citations=sorted(list(set(citations)))
#    max_idx=len(sort_citations)-1
#    min_idx=0
#    for i in unique_citations:
#        get_idx=sort_citations.index(i)
#        if (max_idx-get_idx+1>=i) :
#            answer.append(i)
#    return max(answer)

#오답 2
#def solution(citations):
#    answer=0
#    sort_citations=sorted(citations, reverse=True)
#    for idx, i in enumerate(sort_citations):
#        if i>=idx:
#            answer=i
#    return answer

def solution(citations):
    answer=0
    sort_citations=sorted(citations, reverse=True)
    for idx, i in enumerate(sort_citations):
        if i<=idx:
            return idx
    return len(citations)