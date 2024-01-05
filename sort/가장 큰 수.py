def solution(numbers):
    answer = [str(number) for number in numbers]
    answer.sort(key=lambda x: x*3, reverse=True)
    if all(num == '0' for num in answer):
        return '0'
    return ''.join(answer)