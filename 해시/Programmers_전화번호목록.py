# 해시 사용 못함 ㅠ
# zip 사용 안했을 때는 배열 이용해서 하나씩 비교했음

def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
