def solution(phone_book):
    phone = {}
    for number in phone_book:
        phone[number] = True
    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            if prefix in phone:
                return False
    return True


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True