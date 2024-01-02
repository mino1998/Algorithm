def solution(nums):
    get_mons=int(len(nums)/2)
    num_dict={}
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    length=len(num_dict)
    if length>=get_mons:
        return get_mons
    else:
        return length